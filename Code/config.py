

# ------------------------ PATH ------------------------
ROOT_DIR = ".."

DATA_DIR = f"{ROOT_DIR}/Data"

# ------------------------ DATA ------------------------
# provided data
ORI_DATA = f"{DATA_DIR}/winemag-data-130k-v2.csv"
ALL_DATA = f"{DATA_DIR}/data.csv"
TRAIN_DATA = f"{DATA_DIR}/train.csv"
TEST_DATA = f"{DATA_DIR}/test.csv"

# ------------------------ PARAM ------------------------

# Vectorization parameters
# Range (inclusive) of n-gram sizes for tokenizing text.
NGRAM_RANGE = (1, 2)

# Limit on the number of features. We use the top 20K features.
TOP_K = 20000

# Whether text should be split into word or character n-grams.
# One of 'word', 'char'.
TOKEN_MODE = 'word'

# Minimum document/corpus frequency below which a token will be discarded.
MIN_DOCUMENT_FREQUENCY = 2


# ------------------------ OTHER ------------------------
RANDOM_SEED = 2019


    
