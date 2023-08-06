import sys
sys.path.insert(0, './src/check_connection')
from check_connection import check_connection

def test_connection():
    outcome = check_connection("orf.at", 4)
    assert outcome != False