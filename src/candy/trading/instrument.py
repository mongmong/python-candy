
import datetime
import enum

from candy import datefunc

class InstrumentType(enum.Enum):
    Stock = 0
    Option = 1
    Future = 2
    # FutureOption = 3

class OptionType(enum.Enum):
    Call = 0
    Put = 1


class Instrument(object):
    def __init__(self, symbol, instrument_type:InstrumentType = InstrumentType.Stock, expiration = None, option_type:OptionType = None, strike:float = None):
        self.symbol = symbol.upper()
        self.type = instrument_type
        if self.type == InstrumentType.Stock:
            self.expiration = None
            self.option_type = None
            self.strike = None
        elif self.type == InstrumentType.Option:
            self.expiration = datefunc.as_datetime(expiration)
            self.option_type = option_type
            self.strike = float(strike)
        elif self.type == InstrumentType.Future:
            self.expiration = datefunc.as_datetime(expiration)
            self.option_type = None
            self.strike = None
        else:
            raise Exception('Unsupported instrument type [%s].' % self.type)

    @property
    def Symbol(self):
        return self.symbol

    @property
    def Type(self):
        return self.type

    @property
    def Expiration(self):
        return self.expiration

    @property
    def Strike(self):
        return self.strike

    def __str__(self):
        if self.type == InstrumentType.Stock:
            return '<%s>' % self.symbol
        elif self.type == InstrumentType.Option:
            return '<%s:%s;%.2f%s>' % (self.symbol, self.expiration.strftime('%Y-%m-%d'), self.strike, ('C', 'P')[self.option_type.value])
        elif self.type == InstrumentType.Future:
            return '<%s:%s>' % (self.symbol, self.expiration.strftime('%Y-%m-%d'))
        else:
            raise Exception('<Unknown: %s>' % self.symbol)

    def days_to_expiration(self, today = datetime.date.today()):
        if not self.expiration:
            return -1

        days_diff = (self.expiration - today).day

        return days_diff if days_diff > 0 else 0

    DTE = days_to_expiration
    
def stock(symbol):
    return Instrument(symbol)

def call_option(symbol, expiration, strike:float):
    return Instrument(symbol, InstrumentType.Option, expiration, OptionType.Call, strike)

def put_option(symbol, expiration, strike:float):
    return Instrument(symbol, InstrumentType.Option, expiration, OptionType.Put, strike)
        
def future(symbol, expiration):
    return Instrument(symbol, InstrumentType.Future, expiration)

def from_description(desc):
    desc0 = desc
    if ':' in desc:
        symbol, desc = desc.split(':', 1)
        if ';' in desc:
            expiration, desc = desc.split(';')
            if desc.endswith('C') or desc.endswith('c'):
                return call_option(symbol, expiration, float(desc.rstrip('Cc')))
            elif desc.endswith('P') or desc.endswith('p'):
                return put_option(symbol, expiration, float(desc.rstrip('Pp')))
            else:
                raise Exception('Invalid instrument description <%s>, option type is not recognized.' % desc0)
        else:
            return future(symbol, desc)
    else:
        return stock(desc)

    raise Exception('Invalid instrument description <%s>.' % desc0)
