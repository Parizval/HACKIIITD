from web3 import Web3
gan_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(gan_url))

acc_1 = '0x03421195a1ECFd18d2324Ac75329aa7442e83718'
acc_2 = '0x4a7579087097f5B1Cc7e8378438d0efEdf1f7C61'

priv_key = 'd4d1141a39ef2272666a4e41f220cebf3fae27275e1b8bcafd79f4c9c2147580'
p2 = "3f4efb6aaf7a1488ae1a281efac8228241dcc1a4937c4047fb5c3b3f50cae06a"

nonce = web3.eth.getTransactionCount(acc_2)

tx = {
    'nonce': nonce,
    'to': acc_1,
    'value': web3.toWei(5, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}
signed_tx = web3.eth.account.signTransaction(tx, p2)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
# data = web3.eth.getTransaction(
#   '0x06fa05cce2c4c54f7a3e0970667cd81319d1e06d0005043e9f1ca8028423573f')

#print(web3.fromWei(data['value'], 'ether'))
