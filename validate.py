from web3 import Web3
gan_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(gan_url))


def is_valid(hash_str, value):
    our_pk = '0x03421195a1ECFd18d2324Ac75329aa7442e83718'
    data = web3.eth.getTransaction(hash_str)
    if data is None:
        return False
    if value == (web3.fromWei(data['value'], 'ether')) and data['to'] == our_pk:
        return True
    return False


def send_money(value, to):
    our_public = '0x03421195a1ECFd18d2324Ac75329aa7442e83718'
    priv_key = 'd4d1141a39ef2272666a4e41f220cebf3fae27275e1b8bcafd79f4c9c2147580'
    nonce = web3.eth.getTransactionCount(our_public)
    tx = {
        'nonce': nonce,
        'to': to,
        'value': web3.toWei(value, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
    }
    signed_tx = web3.eth.account.signTransaction(tx, priv_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return web3.toHex(tx_hash)
