# -*- coding: utf-8 -*-

import re


"""Phone"""
def phone_extract(text):
    phone_exp = re.compile('(?<!\\d)((?:13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\\d{8})(?!\\d)',re.M | re.S | re.I)
    # landline_exp = re.compile(u'(\\(?0\\d{2,4}[-)]\\d{7,8})')
    tmp = phone_exp.findall(text)
    # tmp2 = landline_exp.findall(text)
    # return list(set(tmp + tmp2))
    return list(set(tmp))


"""QQ"""
def qq_extract(content):
    qq_exp = re.compile('[q扣]{1,2}[:：\s号联系群]*?([1-9][0-9]{4,10}\\b)', re.M | re.S | re.I)
    qq = re.findall(qq_exp, content)
    return list(set(qq))


"""Identity Card"""
def card_extract(content):
    card_exp = re.compile(
        r'(?<!\d)(?:(?:([1-9]\d{5}(?:18|19|(?:[23]\d))\d{2}(?:(?:0[1-9])|(?:10|11|12))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])(?!\d)))',
        re.M | re.S | re.I)
    identity_card = re.findall(card_exp, content)
    identity_card = list(map(lambda x:''.join(x) ,identity_card))
    return identity_card


"""TG"""
def tg_extract(content):
    tg_exp = re.compile('(?:\\btg|纸飞机|飞机|tg:)[,，:：\s号联系群@]{1,}([\+@a-zA-Z\d_]{5,})', re.M | re.S | re.I)
    tg_url_exp = re.compile('(?:http://|https://)(?:t\\.me|telegram\\.me)[a-z0-9-~\\/]*', re.M | re.S | re.I)
    tg_num = tg_exp.findall(content)
    tg_http = tg_url_exp.findall(content)
    tg_num.extend(tg_http)
    return list(set(tg_num))


"""Wechat"""
def wechart_extract(content):
    regex_wx = re.compile(r'(微信)[,，；;:：\s]*((?:1[3-9]\d{9}|[a-zA-Z\d._-]*\@[a-zA-Z\d.-]{1,10}\.[a-zA-Z\d]{1,20}|[a-zA-Z\d-]{5,20}|[1-9]\d{4,10}))',re.M | re.S | re.I)
    wechart = []
    wei = re.search(regex_wx, content)
    try:
        chart = wei.group(2)
        wechart.append(chart)
    except Exception as e:
        pass
    return wechart


"""Alipay"""
def alipay_extract(content):
    regex_pay = re.compile(r'^(支付宝)[,，；;:：\s]*((?:1[3-9]\d{9}|[a-zA-Z\d._-]*\@[a-zA-Z\d.-]{1,10}\.[a-zA-Z\d]{1,20}))',re.M | re.S |re.I)
    alipay = []
    pay = re.match(regex_pay, content)
    try:
        pay = pay.group(2)
        alipay.append(pay)
    except Exception as e:
        pass
    return alipay


"""PGP"""
def pgp_extract(content):
    pgp_exp = re.compile('begin pgp(.*?)end pgp', re.M | re.S | re.I)
    pgp = pgp_exp.findall(content)
    return list(set(pgp))


"""IP"""
def ip_extract(content):
    ip_exp = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', re.M | re.S | re.I)
    ips = ip_exp.findall(content)
    return list(set(ips))


"""BAT"""
def bat_extract(content):
    bat_exp = re.compile('(?:蝙蝠|蝙蝠ID|蝙蝠id)[,，；;:：\\s账号IDid@]*([0-9_]{6,})')
    tmp = bat_exp.findall(content)
    if not tmp:
        bat_exp = re.compile('([0-9_]{6,})[,，；;:：\\s账号IDid@]*(?:蝙蝠|蝙蝠ID|蝙蝠id)')
        tmp = bat_exp.findall(content)
    return list(set(tmp))

"""Facebook"""
def facebook_extract(content):
    regex_face = re.compile(r'(facebook|脸书)[,，；;:：\s]*((?:1[3-9]\d{9}|[a-zA-Z\d._-]*\@[a-zA-Z\d.-]{1,10}\.[a-zA-Z\d]{1,20}|[a-zA-Z\d-]{5,20}|[1-9]\d{4,10}))',re.M | re.S | re.I)
    facebook = []
    face = re.search(regex_face, content)
    try:
        result = face.group(2)
        facebook.append(result)
    except Exception as e:
        pass
    return facebook


"""Twitter"""
def twitter_extract(content):

    regex_tw = re.compile('(https?://twitter.com/)([a-z0-9-~\\/]*)', re.M | re.S | re.I)
    twitter = []
    tw = re.search(regex_tw, content)
    try:
        result = tw.group(2)
        twitter.append(result)
    except:
        pass
    regex_tw2 = re.compile(
        r'(twitter|推特)[,，；;:：\s]*((?:1[3-9]\d{9}|[a-zA-Z\d._-]*\@[a-zA-Z\d.-]{1,10}\.[a-zA-Z\d]{1,20}|[a-zA-Z\d-]{5,20}|[1-9]\d{4,10}))',
        re.M | re.S | re.I)
    tw = re.search(regex_tw2, content)
    try:
        result = tw.group(2)
        twitter.append(result)
    except:
        pass
    return twitter


"""Bitcoin"""

import re
from hashlib import sha256


BTC_ADDRESS_REGEX = re.compile(r'\b[13][a-zA-Z1-9]{26,34}\b')
BTC_ADDRESS_REGEX_ALL = re.compile(r'^[13][a-zA-Z1-9]{26,34}$')

alphabet = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

iseq, bseq, buffer = (
    lambda s: s,
    bytes,
    lambda s: s.buffer,
)


def scrub_input(v):
    if isinstance(v, str) and not isinstance(v, bytes):
        v = v.encode('ascii')

    if not isinstance(v, bytes):
        raise TypeError(
            "a bytes-like object is required (also str), not '%s'" %
            type(v).__name__)

    return v


def b58decode_int(v):
    '''Decode a Base58 encoded string as an integer'''

    v = scrub_input(v)

    decimal = 0
    for char in v:
        decimal = decimal * 58 + alphabet.index(char)
    return decimal


def b58decode(v):
    '''Decode a Base58 encoded string'''

    v = scrub_input(v)

    origlen = len(v)
    v = v.lstrip(alphabet[0:1])
    newlen = len(v)

    acc = b58decode_int(v)

    result = []
    while acc > 0:
        acc, mod = divmod(acc, 256)
        result.append(mod)

    return (b'\0' * (origlen - newlen) + bseq(reversed(result)))


def b58decode_check(v):
    '''Decode and verify the checksum of a Base58 encoded string'''

    try:
        result = b58decode(v)
        result, checksum = result[:-4], result[-4:]
        digest = sha256(sha256(result).digest()).digest()

        if checksum == digest[:4]:
            return True
        return False

    except Exception:
        return False


def is_valid(addr):
    return b58decode_check(addr)


def bitcoin_extract(content):
    btc_addresses = []
    btc_addrs = BTC_ADDRESS_REGEX.findall(content)
    btc_addrs = list(set(btc_addrs))
    for btc_addr in btc_addrs:
        if not is_valid(btc_addr):
            continue
        btc_addresses.append(btc_addr)
    return btc_addresses


"""Ethereum"""
import sha3
import re


ETH_ADDRESS_REGEX = re.compile(r'\b0x[a-fA-F0-9]{40}\b')
ETH_ADDRESS_REGEX_ALL = re.compile(r'^0x[a-fA-F0-9]{40}$')


def checksum_encode(addr_str):  # Takes a hex (string) address as input
    keccak = sha3.keccak_256()
    out = ''
    addr = addr_str.lower().replace('0x', '')
    keccak.update(addr.encode('ascii'))
    hash_addr = keccak.hexdigest()
    for i, c in enumerate(addr):
        if int(hash_addr[i], 16) >= 8:
            out += c.upper()
        else:
            out += c
    return '0x' + out


def eth_is_valid(addr):
    checksum = checksum_encode(addr)
    if addr and addr.lower() == checksum.lower():
        return True
    else:
        return False


def eth_extract(content):
    eth_addresses = []
    eth_addrs = ETH_ADDRESS_REGEX.findall(content)
    eth_addrs = list(set(eth_addrs))
    for eth_addr in eth_addrs:
        if not eth_is_valid(eth_addr):
            continue
        eth_addresses.append(eth_addr)
    return eth_addresses


"""Email"""
import re

TOP_LEVEL_DOMAINS = ['.com', '.org', '.net', '.int', '.edu', '.gov', '.mil', '.arpa', '.ac', '.ad', '.ae', '.af', '.ag', '.ai', '.al', '.am', '.an', '.ao', '.aq', '.ar', '.as', '.at', '.au', '.aw', '.ax', '.az', '.ba', '.bb', '.bd', '.be', '.bf', '.bg', '.bh', '.bi', '.bj', '.bl', '.bm', '.bn', '.bo', '.bq', '.br', '.bs', '.bt', '.bv', '.bw', '.by', '.bz', '.ca', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cl', '.cm', '.cn', '.co', '.cr', '.cu', '.cv', '.cw', '.cx', '.cy', '.cz', '.de', '.dj', '.dk', '.dm', '.do', '.dz', '.ec', '.ee', '.eg', '.eh', '.er', '.es', '.et', '.eu', '.fi', '.fj', '.fk', '.fm', '.fo', '.fr', '.ga', '.gb', '.gd', '.ge', '.gf', '.gg', '.gh', '.gi', '.gl', '.gm', '.gn', '.gp', '.gq', '.gr', '.gs', '.gt', '.gu', '.gw', '.gy', '.hk', '.hm', '.hn', '.hr', '.ht', '.hu', '.id', '.ie', '.il', '.im', '.in', '.io', '.iq', '.ir', '.is', '.it', '.je', '.jm', '.jo', '.jp', '.ke', '.kg', '.kh', '.ki', '.km', '.kn', '.kp', '.kr', '.kw', '.ky', '.kz', '.la', '.lb', '.lc', '.li', '.lk', '.lr', '.ls', '.lt', '.lu', '.lv', '.ly', '.ma', '.mc', '.md', '.me', '.mf', '.mg', '.mh', '.mk', '.ml', '.mm', '.mn', '.mo', '.mp', '.mq', '.mr', '.ms', '.mt', '.mu', '.mv', '.mw', '.mx', '.my', '.mz', '.na', '.nc', '.ne', '.nf', '.ng', '.ni', '.nl', '.no', '.np', '.nr', '.nu', '.nz', '.om', '.pa', '.pe', '.pf', '.pg', '.ph', '.pk', '.pl', '.pm', '.pn', '.pr', '.ps', '.pt', '.pw', '.py', '.qa', '.re', '.ro', '.rs', '.ru', '.rw', '.sa', '.sb', '.sc', '.sd', '.se', '.sg', '.sh', '.si', '.sj', '.sk', '.sl', '.sm', '.sn', '.so', '.sr', '.ss', '.st', '.su', '.sv', '.sx', '.sy', '.sz', '.tc', '.td', '.tf', '.tg', '.th', '.tj', '.tk', '.tl', '.tm', '.tn', '.to', '.tp', '.tr', '.tt', '.tv', '.tw', '.tz', '.ua', '.ug', '.uk', '.um', '.us', '.uy', '.uz', '.va', '.vc', '.ve', '.vg', '.vi', '.vn', '.vu', '.wf', '.ws', '.ye', '.yt', '.za', '.zm', '.zw', 'الجزائر.', '.հայ', 'البحرين.', '.বাংলা', '.бел', '.бг[42]', '.中国', '.中國', 'مصر.', '.ею', '.გე', '.ελ[42]', '.香港', '.भारत', 'بھارت.', '.భారత్', '.ભારત', '.ਭਾਰਤ', '.இந்தியா', '.ভারত', '.ಭಾರತ', '.ഭാരതം', '.ভাৰত', '.ଭାରତ', 'بارت.', '.भारतम्', '.भारोत', 'ڀارت.', 'ایران.', 'عراق.', 'الاردن.', '.қаз', '.澳门', '.澳門', 'مليسيا.', 'موريتانيا.', '.мон', 'المغرب.', '.мкд', 'عمان.', 'پاکستان.', 'فلسطين.', 'قطر.', '.рф', 'السعودية.', '.срб', '.新加坡', '.சிங்கப்பூர்', '.한국', '.ලංකා', '.இலங்கை', 'سودان.', 'سورية.', '.台湾', '.台灣', '.ไทย', 'تونس.', '.укр', 'امارات.', 'اليمن.', '.academy', '.accountant', '.accountants', '.active', '.actor', '.ads', '.adult', '.aero', '.agency', '.airforce', '.analytics', '.apartments', '.app', '.archi', '.army', '.art', '.associates', '.attorney', '.auction', '.audible', '.audio', '.author', '.auto', '.autos', '.aws', '.baby', '.band', '.bank', '.bar', '.barefoot', '.bargains', '.baseball', '.basketball', '.beauty', '.beer', '.best', '.bestbuy', '.bet', '.bible', '.bid', '.bike', '.bingo', '.bio', '.biz', '.black', '.blackfriday', '.blockbuster', '.blog', '.blue', '.boo', '.book', '.boots', '.bot', '.boutique', '.box', '.broadway', '.broker', '.build', '.builders', '.business', '.buy', '.buzz', '.cab', '.cafe', '.call', '.cam', '.camera', '.camp', '.cancerresearch', '.capital', '.car', '.cards', '.care', '.career', '.careers', '.cars', '.case', '.cash', '.casino', '.catering', '.catholic', '.center', '.cern', '.ceo', '.cfd', '.channel', '.chat', '.cheap', '.christmas', '.church', '.cipriani', '.circle', '.city', '.claims', '.cleaning', '.click', '.clinic', '.clothing', '.cloud', '.club', '.coach', '.codes', '.coffee', '.college', '.community', '.company', '.compare', '.computer', '.condos', '.construction', '.consulting', '.contact', '.contractors', '.cooking', '.cool', '.coop', '.country', '.coupon', '.coupons', '.courses', '.credit', '.creditcard', '.cruise', '.cricket', '.cruises', '.dad', '.dance', '.data', '.date', '.dating', '.day', '.deal', '.deals', '.degree', '.delivery', '.democrat', '.dental', '.dentist', '.design', '.dev', '.diamonds', '.diet', '.digital', '.direct', '.directory', '.discount', '.diy', '.docs', '.doctor', '.dog', '.domains', '.dot', '.download', '.drive', '.duck', '.earth', '.eat', '.eco', '.education', '.email', '.energy', '.engineer', '.engineering', '.enterprises', '.equipment', '.esq', '.estate', '.events', '.exchange', '.expert', '.exposed', '.express', '.fail', '.faith', '.family', '.fan', '.fans', '.farm', '.fashion', '.fast', '.feedback', '.film', '.final', '.finance', '.financial', '.fire', '.fish', '.fishing', '.fit', '.fitness', '.flights', '.florist', '.flowers', '.fly', '.foo', '.food', '.foodnetwork', '.football', '.forsale', '.forum', '.foundation', '.free', '.frontdoor', '.fun', '.fund', '.furniture', '.fyi', '.gallery', '.game', '.games', '.garden', '.gdn', '.gift', '.gifts', '.gives', '.glass', '.global', '.gold', '.golf', '.gop', '.graphics', '.green', '.gripe', '.grocery', '.group', '.guide', '.guitars', '.guru', '.hair', '.hangout', '.health', '.healthcare', '.help', '.here', '.hiphop', '.hiv', '.hockey', '.holdings', '.holiday', '.homegoods', '.homes', '.homesense', '.horse', '.hospital', '.host', '.hosting', '.hot', '.hotels', '.house', '.how', '.ice', '.icu', '.industries', '.info', '.ing', '.ink', '.institute[75]', '.insurance', '.insure', '.international', '.investments', '.jewelry', '.jobs', '.joy', '.kim', '.kitchen', '.land', '.latino', '.law', '.lawyer', '.lease', '.legal', '.lgbt', '.life', '.lifeinsurance', '.lighting', '.like', '.limited', '.limo', '.link', '.live', '.living', '.loan', '.loans', '.locker', '.lol', '.lotto', '.love', '.ltd', '.luxury', '.makeup', '.management', '.map', '.market', '.marketing', '.markets', '.mba', '.med', '.media', '.meet', '.meme', '.memorial', '.men', '.menu', '.mint', '.mobi', '.mobile', '.mobily', '.moe', '.mom', '.money', '.mortgage', '.motorcycles', '.mov', '.movie', '.museum', '.music', '.name', '.navy', '.network', '.new', '.news', '.ngo', '.ninja', '.now', '.observer', '.off', '.one', '.ong', '.onl', '.online', '.ooo', '.open', '.organic', '.origins', '.page', '.partners', '.parts', '.party', '.pay', '.pet', '.pharmacy', '.phone', '.photo', '.photography', '.photos', '.physio', '.pics', '.pictures', '.pid', '.pin', '.pink', '.pizza', '.place', '.plumbing', '.plus', '.poker', '.porn', '.post', '.press', '.prime', '.pro', '.productions', '.prof', '.promo', '.properties', '.property', '.protection', '.pub', '.qpon', '.racing', '.radio', '.read', '.realestate', '.realtor', '.realty', '.recipes', '.red', '.rehab', '.reit', '.ren', '.rent', '.rentals', '.repair', '.report', '.republican', '.rest', '.restaurant', '.review', '.reviews', '.rich', '.rip', '.rocks', '.rodeo', '.room', '.rugby', '.run', '.safe', '.sale', '.save', '.scholarships', '.school', '.science', '.search', '.secure', '.security', '.select', '.services', '.sex', '.sexy', '.shoes', '.shop', '.shopping', '.show', '.showtime', '.silk', '.singles', '.site', '.ski', '.skin', '.sky', '.sling', '.smile', '.soccer', '.social', '.software', '.solar', '.solutions', '.song', '.space', '.spot', '.spreadbetting', '.storage', '.store', '.stream', '.studio', '.study', '.style', '.sucks', '.supplies', '.supply', '.support', '.surf', '.surgery', '.systems', '.talk', '.tattoo', '.tax', '.taxi', '.team', '.tech', '.technology', '.tel', '.tennis', '.theater', '.theatre', '.tickets', '.tips', '.tires', '.today', '.tools', '.top', '.tours', '.town', '.toys', '.trade', '.trading', '.training', '.travel', '.travelersinsurance', '.trust', '.tube', '.tunes', '.uconnect', '.university', '.vacations', '.ventures', '.vet', '.video', '.villas', '.vip', '.vision', '.vodka', '.vote', '.voting', '.voyage', '.wang', '.watch', '.watches', '.weather', '.webcam', '.website', '.wed', '.wedding', '.whoswho', '.wiki', '.win', '.wine', '.winners', '.work', '.works', '.world', '.wow', '.wtf', '.xxx', '.xyz', '.yachts', '.yoga', '.you', '.zero', '.zone', '.shouji', '.tushu', '.wanggou', '.weibo', '.xihuan', '.arte', '.clinique', '.luxe', '.maison', '.moi', '.rsvp', '.sarl', '.epost', '.gmbh', '.haus', '.immobilien', '.jetzt', '.kaufen', '.kinder', '.reise', '.reisen', '.schule', '.versicherung', '.desi', '.shiksha', '.casa', '.immo', '.moda', '.voto', '.bom', '.passagens', '.abogado', '.gratis', '.futbol', '.hoteles', '.juegos', '.ltda', '.soy', '.tienda', '.uno', '.viajes', '.vuelos', 'موقع.', '.كوم', '.موبايلي', '.كاثوليك', 'شبكة.', '.بيتك', 'بازار.', '.在线', '.中文网', '.网址', '.网站', '.网络', '.公司', '.商城', '.机构', '.我爱你', '.商标', '.世界', '.集团', '.慈善', '.八卦', '.公益', '.дети', '.католик', '.ком', '.онлайн', '.орг', '.сайт', '.संगठन', '.कॉम', '.नेट', '.닷컴', '.닷넷', '.קום\u200e', '.みんな', '.セール', '.ファッション', '.ストア', '.ポイント', '.クラウド', '.コム', '.คอม', '.africa', '.capetown', '.durban', '.joburg', '.abudhabi', '.arab', '.asia', '.doha', '.dubai', '.krd', '.kyoto', '.nagoya', '.okinawa', '.osaka', '.ryukyu', '.taipei', '.tatar', '.tokyo', '.yokohama', '.alsace', '.amsterdam', '.bcn', '.barcelona', '.bayern', '.berlin', '.brussels', '.budapest', '.bzh', '.cat', '.cologne', '.corsica', '.cymru', '.eus', '.frl', '.gal', '.gent', '.hamburg', '.helsinki', '.irish', '.ist', '.istanbul', '.koeln', '.london', '.madrid', '.moscow\xa0[ru]', '.nrw', '.paris', '.ruhr', '.saarland', '.scot', '.stockholm', '.swiss', '.tirol', '.vlaanderen', '.wales', '.wien', '.zuerich', '.boston', '.miami', '.nyc', '.quebec', '.vegas', '.kiwi', '.melbourne', '.sydney', '.lat', '.rio', '.佛山', '.广东', '.москва\xa0[ru]', '.рус\xa0[ru]', '.ابوظبي', '.عرب', '.aaa', '.aarp', '.abarth', '.abb', '.abbott', '.abbvie', '.abc', '.accenture', '.aco', '.aeg', '.aetna', '.afl', '.agakhan', '.aig', '.aigo', '.airbus', '.airtel', '.akdn', '.alfaromeo', '.alibaba', '.alipay', '.allfinanz', '.allstate', '.ally', '.alstom', '.americanexpress', '.amex', '.amica', '.android', '.anz', '.aol', '.apple', '.aquarelle', '.aramco', '.audi', '.auspost', '.axa', '.azure', '.baidu', '.bananarepublic', '.barclaycard', '.barclays', '.basketball', '.bauhaus', '.bbc', '.bbt', '.bbva', '.bcg', '.bentley', '.bharti', '.bing', '.blanco', '.bloomberg', '.bms', '.bmw', '.bnl', '.bnpparibas', '.boehringer', '.bond', '.booking', '.bosch', '.bostik', '.bradesco', '.bridgestone', '.brother', '.bugatti', '.cal', '.calvinklein', '.canon', '.capitalone', '.caravan', '.cartier', '.cba', '.cbn', '.cbre', '.cbs', '.cern', '.cfa', '.chanel', '.chase', '.chintai', '.chrome', '.chrysler', '.cisco', '.citadel', '.citi', '.citic', '.clubmed', '.comcast', '.commbank', '.creditunion', '.crown', '.crs', '.csc', '.cuisinella', '.dabur', '.datsun', '.dealer', '.dell', '.deloitte', '.delta', '.dhl', '.discover', '.dish', '.dnp', '.dodge', '.dunlop', '.dupont', '.dvag', '.edeka', '.emerck', '.epson', '.ericsson', '.erni', '.esurance', '.etisalat', '.eurovision', '.everbank', '.extraspace', '.fage', '.fairwinds', '.farmers', '.fedex', '.ferrari', '.ferrero', '.fiat', '.fidelity', '.firestone', '.firmdale', '.flickr', '.flir', '.flsmidth', '.ford', '.fox', '.fresenius', '.forex', '.frogans', '.frontier', '.fujitsu', '.fujixerox', '.gallo', '.gallup', '.gap', '.gbiz', '.gea', '.genting', '.giving', '.gle', '.globo', '.gmail', '.gmo', '.gmx', '.godaddy', '.goldpoint', '.goodyear', '.goog', '.google', '.grainger', '.guardian', '.gucci', '.hbo', '.hdfc', '.hdfcbank', '.hermes', '.hisamitsu', '.hitachi', '.hkt', '.honda', '.honeywell', '.hotmail', '.hsbc', '.hughes', '.hyatt', '.hyundai', '.ibm', '.ieee', '.ifm', '.ikano', '.imdb', '.infiniti', '.intel', '.intuit', '.ipiranga', '.iselect', '.itau', '.itv', '.iveco', '.jaguar', '.java', '.jcb', '.jcp', '.jeep', '.jpmorgan', '.juniper', '.kddi', '.kerryhotels', '.kerrylogistics', '.kerryproperties', '.kfh', '.kia', '.kinder', '.kindle', '.komatsu', '.kpmg', '.kred', '.kuokgroup', '.lacaixa', '.ladbrokes', '.lamborghini', '.lancaster', '.lancia', '.lancome', '.landrover', '.lanxess', '.lasalle', '.latrobe', '.lds', '.lego', '.liaison', '.lexus', '.lidl', '.lifestyle', '.lilly', '.lincoln', '.linde', '.lipsy', '.lixil', '.locus', '.lotte', '.lpl', '.lplfinancial', '.lundbeck', '.lupin', '.macys', '.maif', '.man', '.mango', '.marriott', '.maserati', '.mattel', '.mckinsey', '.metlife', '.microsoft', '.mini', '.mit', '.mitsubishi', '.mlb', '.mma', '.monash', '.mormon', '.moto', '.movistar', '.msd', '.mtn', '.mtr', '.mutual', '.nadex', '.nationwide', '.natura', '.nba', '.nec', '.netflix', '.neustar', '.newholland', '.nexus', '.nfl', '.nhk', '.nico', '.nike', '.nikon', '.nissan', '.nissay', '.nokia', '.northwesternmutual', '.norton', '.nra', '.ntt', '.obi', '.office', '.omega', '.oracle', '.orange', '.otsuka', '.ovh', '.panasonic', '.pccw', '.pfizer', '.philips', '.piaget', '.pictet', '.ping', '.pioneer', '.play', '.playstation', '.pohl', '.politie', '.praxi', '.prod', '.progressive', '.pru', '.prudential', '.pwc', '.quest', '.qvc', '.redstone', '.reliance', '.rexroth', '.ricoh', '.rmit', '.rocher', '.rogers', '.rwe', '.safety', '.sakura', '.samsung', '.sandvik', '.sandvikcoromant', '.sanofi', '.sap', '.saxo', '.sbi', '.sbs', '.sca', '.scb', '.schaeffler', '.schmidt', '.schwarz', '.scjohnson', '.scor', '.seat', '.sener', '.ses', '.sew', '.seven', '.sfr', '.seek', '.shangrila', '.sharp', '.shaw', '.shell', '.shriram', '.sina', '.sky', '.skype', '.smart', '.sncf', '.softbank', '.sohu', '.sony', '.spiegel', '.stada', '.staples', '.star', '.starhub', '.statebank', '.statefarm', '.statoil', '.stc', '.stcgroup', '.suzuki', '.swatch', '.swiftcover', '.symantec', '.taobao', '.target', '.tatamotors', '.tdk', '.telecity', '.telefonica', '.temasek', '.teva', '.tiffany', '.tjx', '.toray', '.toshiba', '.total', '.toyota', '.travelchannel', '.travelers', '.tui', '.tvs', '.ubs', '.unicom', '.uol', '.ups', '.vanguard', '.verisign', '.vig', '.viking', '.virgin', '.visa', '.vista', '.vistaprint', '.vivo', '.volkswagen', '.volvo', '.walmart', '.walter', '.weatherchannel', '.weber', '.weir', '.williamhill', '.windows', '.wme', '.wolterskluwer', '.woodside', '.wtc', '.xbox', '.xerox', '.xfinity', '.yahoo', '.yamaxun', '.yandex', '.yodobashi', '.youtube', '.zappos', '.zara', '.zip', '.zippo', '.ارامكو', '.اتصالات', '.联通', '.移动', '.中信', '.香格里拉', '.淡马锡', '.大众汽车', '.vermögensberater', '.vermögensberatung', '.グーグル', '.谷歌', '.工行', '.嘉里', '.嘉里大酒店', '.飞利浦', '.诺基亚', '.電訊盈科', '.삼성', '.example', '.invalid', '.local', '.localhost', '.onion', '.test','.i2p','.bit']

def email_extract(content):
    emails = EMAIL_REGEX.findall(content)
    emails = [i.lower() for i in emails]
    emails = list(set(emails))
    emails = [x for x in emails if '.' + x.split('.')[-1] in TOP_LEVEL_DOMAINS]
    return emails



"""Keywords Sentence"""
from textrank4zh import TextRank4Keyword, TextRank4Sentence

EMAIL_REGEX = re.compile(r'\b[a-zA-Z0-9_.+-]{1,50}@[a-zA-Z0-9-]{1,50}\.[a-zA-Z0-9-.]{1,50}[a-zA-Z0-9]\b')
EMAIL_REGEX_ALL = re.compile(r'^[a-zA-Z0-9_.+-]{1,50}@[a-zA-Z0-9-]{1,50}\.[a-zA-Z0-9-.]{1,50}[a-zA-Z0-9]$')


tr4w = TextRank4Keyword()
def keywords(text):
    """
    :param text: 待提取文本信息
    :return: 返回结果
    """
    result = []
    tr4w.analyze(text=text, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        # print(item.word, item.weight)  # word关键词 weight权重
        result.append((item.word))
    # print(result)

    return result


tr4s = TextRank4Sentence()
def keysentence(text):
    """
    :param text: 待提取文本信息
    :return: 返回结果
    """
    tr4s.analyze(text=text, lower=True, source='all_filters')
    result = ''
    for item in tr4s.get_key_sentences(num=3):
        # print(item.index, item.weight, item.sentence)  # index是语句在文本中位置 weight是权重 sentence摘要
        result +=  item.sentence + ';'
    # print(result)

    return result
