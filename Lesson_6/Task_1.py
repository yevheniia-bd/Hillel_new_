def rejoindre_deux_en_un(coin, code) -> dict:
    coin, code = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin'), ('BTC', 'ETH', 'XRP', 'LTC')
    rejoindre = dict(list(zip(coin, code)))
print(rejoindre)
rejoindre_deux_en_un()