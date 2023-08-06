# Show cases

from bert_tokenizer import Tokenizer
from convert_word_span import convert_word_span, convert_char_span

dict_path = "vocab/vocab_chinese.txt"
tokenizer = Tokenizer(dict_path, do_lower_case=True)
#tokens = tokenizer.tokenize("翻译Je pense a vous tout le temps")
tokens = tokenizer.tokenize("播放MYLOVE这首歌")[1:-1]
print(tokens)

print(convert_word_span("播放MYLOVE这首歌", [8, 11], tokenizer))
print(convert_char_span("播放MYLOVE这首歌", [4, 7], tokenizer))