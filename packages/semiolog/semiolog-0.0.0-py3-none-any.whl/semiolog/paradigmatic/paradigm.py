from scipy.stats import entropy
import numpy as np
import tensorflow as tf
import string
from ..syntagmatic.tokenizer import normalizers
from collections import Counter, defaultdict
from operator import itemgetter
from math import log

from ..util import df as slg_df

def tolerance_principle(n):
    return n/log(n)

# TODO: Consider different subtypings in the determination of tolerance
# TODO: Consider also prefixes and infixes

def productive_suffix(parad_keys):
    max_len = max([len(term) for term in parad_keys])

    parad_len = len(parad_keys)

    # TODO This Threshold is set ad hoc and as a quick fix. Think about a better way to avoid division by 0 in tolerance_principle when parad_len = 1. And also to avoid considering productive parads of len 1 or 0.
    if parad_len <2:
        prod_thres = 2
    else:
        prod_thres = parad_len - tolerance_principle(parad_len) #Tolerance principle (Yang, 2016)

    # l=1

    sub_parad = parad_keys
    sub_parad_collector = {key:key for key in parad_keys}

    for suffix_len in range(1,max_len):
        suffix_counter = Counter()
        suffix_dict = defaultdict()
        for term in parad_keys:
            suffix = term[-suffix_len:]
            suffix_counter[suffix]+=1
            suffix_dict[suffix] = suffix_dict.get(suffix,[])+[term]

        if  max(suffix_counter.values()) >= prod_thres:
            suffix = []
            suffix_freq = []
            for s,f in suffix_counter.most_common():
                suffix.append(s)
                suffix_freq.append(f)

            sub_parad = suffix_dict[suffix[0]]
            # TODO This Threshold is set ad hoc and as a quick fix. Think about a better way to avoid division by 0 in tolerance_principle when parad_len = 1. And also to avoid considering productive parads of len 1 or 0.
            if len(sub_parad) <2:
                prod_thres = 2
            else:
                prod_thres = len(sub_parad)-tolerance_principle(len(sub_parad)) # len(sub_parad)/2

            for term in sub_parad:
                sub_parad_collector[term] = (term[:-suffix_len],suffix[0])
            
        else:
            break
    if any([isinstance(term,tuple) for term in sub_parad_collector.values()]):
        return list(sub_parad_collector.values())
    else:
        return None

class Paradigm:
    def __init__(
        self,
        ids,
        values,
        non_zeroes,
        decoder,
        semiotic,
        cum_thres=.5,
        vocab_thres = 500
        ) -> None:

        self.len = non_zeroes.numpy()
        self.ids = ids.numpy()
        self.keys = decoder(ids.numpy()[:self.len]).split()
        self.values = values.numpy()
        query = itemgetter(*self.keys)
        self.probs = query(semiotic.vocab.prob)
        if isinstance(self.probs,float): # if len of keys is 1, then query outputs a float instead of a tuple
            self.probs = tuple([self.probs])
        self.mass = sum(self.probs)

        self.entropy = entropy(self.values)
        self.mass_entropy = entropy(self.probs)
        # self.cumsum = np.cumsum(self.values)

        key_thres = set(list(semiotic.vocab.prob.keys())[:vocab_thres])
        self.top_freq = [key for key in self.keys if key in key_thres]

        self.productivity = productive_suffix(self.keys)


    def __repr__(self) -> str:
        return str(self.keys)

class Paradigmatizer:
    
    def __init__(self, model, bert_tokenizer, decoder) -> None:
        self.model = model
        self.bert_tokenizer = bert_tokenizer
        self.decoder = decoder
        
    def __call__(self,chain,n_token=None):
        """
        If n_token == None, then it computes paradigms for all tokens and adds them as attributes to tokens in chain. If a token is provided, then returns the paradigm for that token.
        """
        
        # TODO: inputs longer than self.model.config.max_position_embeddings yield an error. The workaround here is to truncate the input with [:,:self.model.config.max_position_embeddings], but then not all tokens receive their paradigm. A more consistent solution is needed.

        if isinstance(n_token,int):
            if n_token>=min(chain.len, self.model.config.max_position_embeddings):
                raise Exception(f"The toke number should be within the range of the chain length (< {min(chain.len, self.model.config.max_position_embeddings)})")
            sent_mask = chain.mask(n_token)
            input = self.bert_tokenizer(sent_mask)
            outputs = self.model(input["input_ids"][:,:self.model.config.max_position_embeddings])
            parad_logits = outputs.logits[0, n_token]
            logits_positif = tf.nn.relu(parad_logits)
            probs, norms = tf.linalg.normalize(logits_positif, ord=1)

            non_zeroes = tf.math.count_nonzero(probs)

            parad_data = tf.math.top_k(probs, k = non_zeroes.numpy(), sorted=True)

            parad = Paradigm(
                parad_data.indices,
                parad_data.values,
                non_zeroes,self.decoder, chain.semiotic)

            return parad

        else:
            sent_mask = [chain.mask(n) for n in range(chain.len)]
            input = self.bert_tokenizer(sent_mask)
            outputs = self.model(input["input_ids"][:,:self.model.config.max_position_embeddings])
            parad_logits = tf.gather_nd(outputs.logits, indices=[[i,i] for i in range(chain.len)])
            logits_positif = tf.nn.relu(parad_logits)
            probs, norms = tf.linalg.normalize(logits_positif, ord=1, axis=1)
            
            # Maybe its cheaper to compute top k for k = non_zero, which would differ from row to row, and hence not yeld a tensor. To be tested.

            non_zeroes = tf.math.count_nonzero(probs,axis=1)
            max_non_zeroes = max(non_zeroes).numpy()

            parad_data = tf.math.top_k(probs, k = max_non_zeroes, sorted=True)

            parads = [Paradigm(ids,values,nonzeroes,self.decoder, chain.semiotic) for ids,values,nonzeroes in zip(parad_data.indices,parad_data.values,non_zeroes)]

            for token,parad in zip(chain,parads):
                token.paradigm = parad


class ParadigmChain:

    def __init__(self,chain) -> None:
        self.semiotic = chain.semiotic
        self.len = chain.len
        # self.probs = chain.probs
        self.paradigms = [token.paradigm for token in chain.tokens]
        self.keys = [token.paradigm.keys for token in chain.tokens]
        # self.keys_t = [token.paradigm.keys_t for token in chain.tokens]
        # self.keys_t_soft = [token.paradigm.keys_t_soft for token in chain.tokens]

        self.labels = [token.label for token in chain.tokens]
        self.spans = [token.span for token in chain.tokens]
        self.indexes = [f"{token.label}_{token.position}" for token in chain.tokens]
    
    def __getitem__(self, index:str):
        return self.paradigms[index]
    
    def df(self, size = 20):
        return slg_df([p[:size] for p in self.keys], self.indexes)