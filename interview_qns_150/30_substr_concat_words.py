from typing import List
from collections import defaultdict, Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # word_window = len(words[0])
        # words_len = len(words)
        # s_len = len(s)

        # words_dict = defaultdict(int)
        
        # for word in words:
        #     words_dict[word] +=1 

        # result_indices = []
        
        # for sent_start_index in range(s_len -word_window* words_len):
        #     curr_map = words_dict.copy()

        #     for word_index in range(sent_start_index, sent_start_index+word_window*words_len, word_window):
        #         word = s[word_index:word_index+word_window]
        #         if word in curr_map and curr_map.get(word) != 0:
        #             curr_map[word]-=1
        #         else:
        #             curr_map = words_dict.copy()
            

        #     if all(value == 0 for key,value in curr_map.items()):
        #         result_indices.append(sent_start_index)
                
        # return result_indices

        #===== above is taking more time to execute

        #or 

        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length*word_count
        word_freq = Counter(words)

        result = []

        for i in range(len(s) - total_length+1): # give buffer till all words length in list
            curr_map = Counter()

            for j in range(word_count):

                start_ind = i+j*word_length
                word = s[start_ind : start_ind + word_length]

                if not word_freq.get(word):
                    break
                    
                curr_map[word] +=1
            
                if curr_map[word] > word_freq[word]:
                    break
            
            if curr_map == word_freq:
                result.append(i)
        return result



obj = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]
# s ="wordgoodgoodgoodbestword"
# words =["word","good","best","good"]
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words =["fooo","barr","wing","ding","wing"]


print(obj.findSubstring(s, words))








        