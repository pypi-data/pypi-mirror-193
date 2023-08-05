"""randomlib package - A natural language processing library for Marathi """
import logging
import huggingface_hub.utils as hf_hub_utils
import pandas as pd
logging.disable(logging.INFO)
logging.disable(logging.DEBUG)
logging.disable(logging.WARNING)
hf_hub_utils.disable_progress_bars()
pd.options.display.max_colwidth = None
