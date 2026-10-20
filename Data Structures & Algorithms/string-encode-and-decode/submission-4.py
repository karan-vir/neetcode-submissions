class Solution:
    def encode(self, strs: List[str]) -> str:
        # Join the strings
        if len(strs) == 0:
            return '😂'
        comb = "`".join(strs)
        
        # Decode the combined string
        encoded_string = ''
        for character in comb:
            if character == '`':
                encoded_string += '`/'
            else:
                asci_val = ord(character)
                encoded_string += str(asci_val) + '/'
        
        return encoded_string;



    def decode(self, s: str) -> List[str]:
        if s=='😂':
            return []
        decoded_lst_out = []
        decoded_lst = re.split('`',s)

        for word in decoded_lst:
            word_dismanteled = re.split('/',word)
            print(word_dismanteled)
            word_formed=''
            for character in word_dismanteled:
                if character in ['','/']:
                    continue
                else:
                    word_formed += chr(int(character))
            
            decoded_lst_out.append(word_formed)
        return decoded_lst_out;

















    # Attempt 1
    #     # Store the characters by increasing the value by 1,
    #     # a : 0, becomes 1 which will become b, and so on
    #     # Different words can be combined togerher to form  one word using a special character like #
    #     str_encod = ''
    #     for word in strs:
    #         word_encoded = ''
    #         for letter in word:
    #             word_encoded += (str(ord(letter)) +'*')

    #         str_encod += word_encoded + '#'
        
    #     print(str_encod)
    #     return str_encod

    # def decode(self, s: str) -> List[str]:
    #     # Decode is just the opposit of encode.
    #     decode_lst = []
    #     separate_words = s.split('#')
    #     print(separate_words)
    #     for word in separate_words:
    #         if word == '':
    #             pass
    #         else:

    #             word_decode = word.split('*')
    #             word_decode = [chr(int(letter)) if letter != '' else '' for letter in word_decode]
    #             word_decode = "".join(word_decode)
    #             decode_lst.append(word_decode)      
    #     return [""] if decode_lst == [] else decode_lst
        