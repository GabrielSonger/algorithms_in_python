class Solution:
    def get_substring(self, str_input):
        if not isinstance(str_input, str):
            return None

        max_length = 0
        start_idx = 0
        str_idx_dict = {}

        for s_idx, s_val in enumerate(str_input):

            if s_val in str_idx_dict and start_idx <= str_idx_dict[s_val]:
                start_idx = str_idx_dict[s_val] + 1
            else:
                max_length = max(max_length, s_idx - start_idx + 1)

            str_idx_dict[s_val] = s_idx

        return max_length
