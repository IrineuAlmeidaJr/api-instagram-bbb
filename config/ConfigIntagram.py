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
            url_image='https://s2.glbimg.com/Mpl3qRVLOrk7-_VUHaXRotY3FcE=/i.s3.glbimg.com/v1'
                      '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/N/K/pR0TBqQKmhwossfbmpvA/gabriel'
                      '-header.png'
        ),
            User(
                name='Paula',
                instagram_username='paulafreitasr_',
                followers=profile.from_username(bot.context, 'paulafreitasr_').followers,
                url_image='https://s2.glbimg.com/T2HHuuUM1XfUczroij9NLeJDF1c=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/t/K/NngKOBS3WnqzVYuHsMrA/paula'
                          '-header.png'
            ),
            User(
                name='Aline Wirley',
                instagram_username='alinewirley',
                followers=profile.from_username(bot.context, 'alinewirley').followers,
                url_image='https://s2.glbimg.com/w7qvHNQfWEsGhWB-ZWT8JMkCnTU=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/0/P/7j1B15Remqcmx3k6b9Qw/aline'
                          '-header.png'
            ),
            User(
                name='Cezar Black',
                instagram_username='cezar.black',
                followers=profile.from_username(bot.context, 'cezar.black').followers,
                url_image='https://s2.glbimg.com/v3mI57iDI5wy9RhBKaXL1NcWuFY=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/I/z/hVtn3tTaG3BJE1oKEkkw/cezar'
                          '-header.png'
            ),
            User(
                name='Bruna Griphao',
                instagram_username='brunagriphao',
                followers=profile.from_username(bot.context, 'brunagriphao').followers,
                url_image='https://s2.glbimg.com/8X-QrfQaIULFSWGxsflaJ3ICIvk=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/a/S/slhMnqRhijfqjR1S5bLw/bruna'
                          '-griphao-header.png'
            ),
            User(
                name='Gustavo',
                instagram_username='gustavo_benedetii',
                followers=profile.from_username(bot.context, 'gustavo_benedetii').followers,
                url_image='https://s2.glbimg.com/qe6MhbhPIJGq0cTv6HDyf9gj2YI=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/c/t/c13HiaSrGY0rLBBduvnw/gustavo'
                          '-header.png'
            ),
            User(
                name='Fred',
                instagram_username='fred',
                followers=profile.from_username(bot.context, 'fred').followers,
                url_image='https://s2.glbimg.com/Ufy9ZwsbXJsg98yvtCHG2PEDxA4=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/j/e/itWJAAQxi8s20EwyBlIw/fred'
                          '-header.png'
            ),
            User(
                name='Larissa',
                instagram_username='larisantosbe',
                followers=profile.from_username(bot.context, 'larisantosbe').followers,
                url_image='https://s2.glbimg.com/vGJ0jIMGt9v_nGQVQzgc7Jhiu-E=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/A/P/tUYmnWSMKv6F49LpK6Gg/larissa'
                          '-header.png'
            ),
            User(
                name='Ricardo',
                instagram_username='rickcamargo',
                followers=profile.from_username(bot.context, 'rickcamargo').followers,
                url_image='https://s2.glbimg.com/y9hzBoVegiFGTdW2ipnKOvyOFhI=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/E/D/6B9jzdSeORm4EUilEVoQ/ricardo'
                          '-header.png'
            ),
            User(
                name='Domitila Barros',
                instagram_username='domitila_barros',
                followers=profile.from_username(bot.context, 'domitila_barros').followers,
                url_image='https://s2.glbimg.com/jz2z6E8mDGFDhhJbLyVv5x3lklw=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/m/d/GRL90lTRKDBpeJv74YRw/domitila'
                          '-barros-header.png'
            ),
            User(
                name='Antonio ‘Cara de Sapato’ Jr',
                instagram_username='caradesapato',
                followers=profile.from_username(bot.context, 'caradesapato').followers,
                url_image='https://s2.glbimg.com/Q31lPEvYaZHoEDg8pdJJw7w1JfM=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/x/Q/EQN1UOSdGEWYnmolynkg/antonio'
                          '-cara-de-sapato-jr-header.png'
            ),
            User(
                name='Sarah Aline',
                instagram_username='saa_aline',
                followers=profile.from_username(bot.context, 'saa_aline').followers,
                url_image='https://s2.glbimg.com/JflM0Xy_JPsOaWmFj8tt-T7g6Dc=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/1/Y/y0RlncQAiaTuhwBhLrzw/sarah'
                          '-aline-header.png'
            ),
            User(
                name='Fred Nicácio',
                instagram_username='frednicacio',
                followers=profile.from_username(bot.context, 'frednicacio').followers,
                url_image='https://s2.glbimg.com/R7kYIvmFPpg-TznLbbiHXf3aSCs=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/V/M/j5g9GxS2CxRhGPFiA4Hw/fred'
                          '-nicacio-header.png'
            ),
            User(
                name='Key Alves',
                instagram_username='keyalves',
                followers=profile.from_username(bot.context, 'keyalves').followers,
                url_image='https://s2.glbimg.com/yHYwBbCAUQBdETAvLsDi-6nrwcc=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/8/u/gnkgiRTwmhfQdCA6ADFg/key-alves'
                          '-header.png'
            ),
            User(
                name='Marília',
                instagram_username='mariliamiranda',
                followers=profile.from_username(bot.context, 'mariliamiranda').followers,
                url_image='https://s2.glbimg.com/tH0ClVn_6gIqHFpI9cmlNcWb1uc=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/U/H/0azEdxTnOrg5LBqACqqw/marilia'
                          '-header.png'
            ),
            User(
                name='Cristian',
                instagram_username='cristianvanelli',
                followers=profile.from_username(bot.context, 'cristianvanelli').followers,
                url_image='https://s2.glbimg.com/ortMPWho1pNHZB01O8rV9qxhuus=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/9/i/9AIgCDQyaHfJ3A7F5QRg/cristian'
                          '-header.png'
            ),
            User(
                name='Marvvila',
                instagram_username='marvvila',
                followers=profile.from_username(bot.context, 'marvvila').followers,
                url_image='https://s2.glbimg.com/XvifUI61x8qyuKp8FpSGxrXiXjo=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/J/k/FJGWXtRcCt0ciRCKFvuw/marvvila'
                          '-header.png'
            ),
            User(
                name='Tina',
                instagram_username='tinacalamba',
                followers=profile.from_username(bot.context, 'tinacalamba').followers,
                url_image='https://s2.glbimg.com/ZQw7nTqoJFbotj2yh6deUqyYmIk=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/G/t/thK3niQ3iT3A4AxI8BUw/tina'
                          '-header.png'
            ),
            User(
                name='Gabriel Santana',
                instagram_username='gbielsantana',
                followers=profile.from_username(bot.context, 'gbielsantana').followers,
                url_image='https://s2.glbimg.com/gaPleq0Qg3tdw96XVtkmKqJMtp0=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/J/z/qVmo6hQuutGTn4vW7goA/gabriel'
                          '-santana-header.png'
            ),
            User(
                name='Amanda',
                instagram_username='ameirelles',
                followers=profile.from_username(bot.context, 'ameirelles').followers,
                url_image='https://s2.glbimg.com/zxsqoLOhESH9ecr83ysD1KjCCw4=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/S/1/dpAkSjTBWAiUzCv0xMuQ/amanda'
                          '-header.png'
            ),
            User(
                name='Bruno',
                instagram_username='brunornogueira',
                followers=profile.from_username(bot.context, 'brunornogueira').followers,
                url_image='https://s2.glbimg.com/IgQjPeeevRGFea2Z3PBhUu9Uo0o=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/j/P/SdP90GSH2aMLLrwjVYAA/bruno'
                          '-header.png'
            ),
            User(
                name='MC Guimê',
                instagram_username='mcguime',
                followers=profile.from_username(bot.context, 'mcguime').followers,
                url_image='https://s2.glbimg.com/UrG4E2fFJpUdMQeKrKFNYVl4F4c=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/P/s/mgALN4TTacXvAJ67CK1w/mc-guime'
                          '-header.png'
            ),
        ]
