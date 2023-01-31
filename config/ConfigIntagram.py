import instaloader
from model.User import User


class ConfigInstagram:
    username = 'irineu.almeida.jr@icloud.com'
    bot = instaloader.Instaloader()
    # bot.interactive_login(username)
    profile = instaloader.Profile

    @staticmethod
    def load():
        bot = instaloader.Instaloader()
        profile = instaloader.Profile
        return [User(
            name='Gabriel',
            instagram_username='vulgofop',
            followers=profile.from_username(bot.context, 'vulgofop').followers,
            url_image='https://s2.glbimg.com/runqsEy54iPoXMQ8qkLRe7WQSPY=/i.s3.glbimg.com/v1'
                      '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/R/i/ar31rfRe6EGls4fhYOBg'
                      '/gabriel-foto-330-270-bbb23.png '
        ),
            User(
                name='Paula',
                instagram_username='paulafreitasr_',
                followers=profile.from_username(bot.context, 'paulafreitasr_').followers,
                url_image='https://s2.glbimg.com/nVOp1nrNMAlzW57bfHFdon5L1qg=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/s/r/AstvO8T0OvZCRN7XE7cA'
                          '/paula-foto-330-270-bbb23.png '
            ),
            User(
                name='Aline Wirley',
                instagram_username='alinewirley',
                followers=profile.from_username(bot.context, 'alinewirley').followers,
                url_image='https://s2.glbimg.com/N_hBFjgkyF7j7i27H8lKm8nFv34=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/Z/p/sphPCLSBmIxr3u3WFuCw'
                          '/aline-nova.png '
            ),
            User(
                name='Cezar Black',
                instagram_username='cezar.black',
                followers=profile.from_username(bot.context, 'cezar.black').followers,
                url_image='https://s2.glbimg.com/HNtVguV5kfdFMyGdB-sAGcFDXa0=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/q/8/isGwrhTseVHYUkKFfvpA'
                          '/cezar-foto-330-270-bbb23.png '
            ),
            User(
                name='Bruna Griphao',
                instagram_username='brunagriphao',
                followers=profile.from_username(bot.context, 'brunagriphao').followers,
                url_image='https://s2.glbimg.com/TCP9ZDJu95vsCDXaaDXfJl_nbMw=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/x/Q/booSm0TKGKCbOAp2hnSg'
                          '/bruna-griphao-foto-330-270-bbb23.png '
            ),
            User(
                name='Gustavo',
                instagram_username='gustavo_benedetii',
                followers=profile.from_username(bot.context, 'gustavo_benedetii').followers,
                url_image='https://s2.glbimg.com/hb1e_t0vJU09PCDH2u4_TuxapYY=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/p/M/FaP5NrR6it8n3nSQlD4Q'
                          '/gustavo-foto-330-270-bbb23.png '
            ),
            User(
                name='Fred',
                instagram_username='fred',
                followers=profile.from_username(bot.context, 'fred').followers,
                url_image='https://s2.glbimg.com/eM0NqkWFwpdDzFw2rQuf0ScXP8M=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/f/J/bT3Vv0QZWAn5f5UepdqQ'
                          '/fred-foto-330-270-bbb23.png '
            ),
            User(
                name='Larissa',
                instagram_username='larisantosbe',
                followers=profile.from_username(bot.context, 'larisantosbe').followers,
                url_image='https://s2.glbimg.com/-caXoQsbWDAoKTooZMVTVncRGSs=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/O/A/MaQNodRIiGx8A8UmBdsQ'
                          '/larissa-foto-330-270-bbb23.png '
            ),
            User(
                name='Ricardo',
                instagram_username='rickcamargo',
                followers=profile.from_username(bot.context, 'rickcamargo').followers,
                url_image='https://s2.glbimg.com/lm4D5KvY-hdaZy1uLyb5vkJYJ3o=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/l/Z/I3L2CyQcGKSLBdxcYz5g'
                          '/ricardo-foto-330-270-bbb23.png '
            ),
            User(
                name='Domitila Barros',
                instagram_username='domitila_barros',
                followers=profile.from_username(bot.context, 'domitila_barros').followers,
                url_image='https://s2.glbimg.com/bvcrAlxJWGrroFKlgd08dXTrMUU=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/D/B/1eIYhdRv2ymWBzulzKmw'
                          '/domitila-barros-foto-330-270-bbb23.png '
            ),
            User(
                name='Antonio ‘Cara de Sapato’ Jr',
                instagram_username='caradesapato',
                followers=profile.from_username(bot.context, 'caradesapato').followers,
                url_image='https://s2.glbimg.com/nBl5zuHYzAupafMVvHicEkle1gk=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/Z/A/oImXJNRcADBfVcPTQsdw'
                          '/cara-de-sapato-foto-330-270-bbb23.png '
            ),
            User(
                name='Sarah Aline',
                instagram_username='saa_aline',
                followers=profile.from_username(bot.context, 'saa_aline').followers,
                url_image='https://s2.glbimg.com/yCts0mvxcUtLOKKL3Q5veQr83Vw=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/7/a/onW6EUSfylTCqjwjYZuA'
                          '/sarah-aline-foto-330-270-bbb23.png '
            ),
            User(
                name='Fred Nicácio',
                instagram_username='frednicacio',
                followers=profile.from_username(bot.context, 'frednicacio').followers,
                url_image='https://s2.glbimg.com/Oq-kfI9lD9Qd1pn75esr4SlJdEw=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/s/9/Mdb40BTGAJsJ9fuoRvrg'
                          '/nicacio-foto-330-270-bbb23.png '
            ),
            User(
                name='Key Alves',
                instagram_username='keyalves',
                followers=profile.from_username(bot.context, 'keyalves').followers,
                url_image='https://s2.glbimg.com/zTwsn2Og1mYqvm7_iGAkOaa6HB0=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/s/q/MBFLD6RFaAjPs0vK1TBQ'
                          '/key-alves-foto-330-270-bbb23.png '
            ),
            User(
                name='Marília',
                instagram_username='mariliamiranda',
                followers=profile.from_username(bot.context, 'mariliamiranda').followers,
                url_image='https://s2.glbimg.com/jhMhly4KC7xuGqsHFR7tcA00en8=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/D/Z/g3UMGYT3WHoTDoE6SOqQ'
                          '/marilia-foto-330-270-bbb23.png '
            ),
            User(
                name='Cristian',
                instagram_username='cristianvanelli',
                followers=profile.from_username(bot.context, 'cristianvanelli').followers,
                url_image='https://s2.glbimg.com/UZGxV710OZU24-fVb1lrzYN2_aU=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/1/Y/ltP6UASu2o2tJwzeOW1A'
                          '/cristian-foto-330-270-bbb23.png '
            ),
            User(
                name='Marvvila',
                instagram_username='marvvila',
                followers=profile.from_username(bot.context, 'marvvila').followers,
                url_image='https://s2.glbimg.com/9JyU3AWnqM35PYDaDJoL9VWEJl0=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/A/b/llpQ1ASpKpNyl91amBiw'
                          '/marvvila-foto-330-270-bbb23.png '
            ),
            User(
                name='Tina',
                instagram_username='tinacalamba',
                followers=profile.from_username(bot.context, 'tinacalamba').followers,
                url_image='https://s2.glbimg.com/_xqu-RbYnhd_RlB-ityU-GghD7Q=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/E/a/NToZOxRaKdpWOWPJq5AQ'
                          '/tina-foto-330-270-bbb23.png '
            ),
            User(
                name='Gabriel Santana',
                instagram_username='gbielsantana',
                followers=profile.from_username(bot.context, 'gbielsantana').followers,
                url_image='https://s2.glbimg.com/hnfJZ0wgKyySKyfXqlLX7CwZ7Ug=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/x/p/esEdQlQPmY5U1C2KAGmQ'
                          '/gabriel-santana-foto-330-270-bbb23.png '
            ),
            User(
                name='Amanda',
                instagram_username='ameirelles',
                followers=profile.from_username(bot.context, 'ameirelles').followers,
                url_image='https://s2.glbimg.com/A40VzPy5Fs8lVKRYSR5m8QDo9Cs=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/l/1/XBiigWR4iH4tA4DoSDnA'
                          '/amanda-foto-330-270-bbb23.png '
            ),
            User(
                name='Bruno',
                instagram_username='brunornogueira',
                followers=profile.from_username(bot.context, 'brunornogueira').followers,
                url_image='https://s2.glbimg.com/F8GthYiW4DsHxAFe9bVvsz1OGfA=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/w/i/H84f93Qg6mQHwlz3IZ4A'
                          '/bruno-foto-330-270-bbb23.png '
            ),
            User(
                name='MC Guimê',
                instagram_username='mcguime',
                followers=profile.from_username(bot.context, 'mcguime').followers,
                url_image='https://s2.glbimg.com/_d7OBvTEilzCgRAyQW8rTA3JyP4=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/j/w/07Dl8YRKKoyboVMwXrJw/mc'
                          '-guime-foto-330-270-bbb23.png '
            ),
        ]
