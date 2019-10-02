import datetime

def std4dt(dt):
    """dt -> string like 'YYYYMMDDtHHMMSS%f'
    """
    return dt.strftime('%Y%m%dt%H%M%S.%f')

def iso4dt(dt):
    """dt -> string like 'YYYYwWWDtHHMMSS.....'
    """
    y,w,d = dt.isocalendar()
    w = ('0'+str(w))[-2:]
    return '%sw%s%s' % (y,w,d) + dt.strftime('t%H%M%S.%f')

def split(rep):
    parts = rep.lower().split('t')
    assert len(parts)==2
    return parts[0], parts[1]

########################################################################
#  UNIT TESTS
########################################################################

# These two dates represention the transition from a year with 53 weeks.

Jan03 = datetime.datetime(2016,1,3)
Jan04 = datetime.datetime(2016,1,4)

# This is a test of date with time.

Feb03 = datetime.datetime(2016,2,3,4,5,6,999999)

stdJan03 = '20160103t000000.000000'
stdJan04 = '20160104t000000.000000'
stdFeb03 = '20160203t040506.999999'
isoJan03 = '2015w537t000000.000000'
isoJan04 = '2016w011t000000.000000'

def test_split__stdJan03(): assert split( stdJan03 ) == ('20160103', '000000.000000')
def test_split__stdJan04(): assert split( stdJan04 ) == ('20160104', '000000.000000')
def test_split__stdFeb03(): assert split( stdFeb03 ) == ('20160203', '040506.999999')
def test_split__isoJan03(): assert split( isoJan03 ) == ('2015w537', '000000.000000')
def test_split__isoJan04(): assert split( isoJan04 ) == ('2016w011', '000000.000000')

def test_std4dt__Jan03(): assert std4dt(Jan03) == stdJan03
def test_std4dt__Jan04(): assert std4dt(Jan04) == stdJan04
def test_std4dt__Feb03(): assert std4dt(Feb03) == stdFeb03
def test_iso4dt__Jan03(): assert iso4dt(Jan03) == isoJan03
def test_iso4dt__Jan04(): assert iso4dt(Jan04) == isoJan04
