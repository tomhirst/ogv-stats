from brownie import *
from dotenv import load_dotenv

load_dotenv()

network.connect("mainnet")

ogv = Contract.from_explorer("0x9c354503c38481a7a7a51629142963f98ecc12d0")

MANDATORY = '0xD667091c2d1DCc8620f4eaEA254CdFB0a176718D'
OPTIONAL = '0x7aE2334f12a449895AD21d4c255D9DE194fe986f'
OGV_STAKING = '0x0c4576ca1c365868e162554af8e385dc3e7c66d9'
 
MANDATORY_FUNDING = 0x149d71d9a6c6ff7fd590000
OPTIONAL_FUNDING = 0x026aa70fd8233cd7bb700000

def c18(value):
    return "{0:,.0f}".format(value / 1e18)
 
def show_claim_stats(name, total, claimed):
    print("%s OGV (%0.2f%%) %s" % (
        c18(total - claimed),
        ((total - claimed) / total * 100),
        name
    ))

def show_staking_stats(token, total, staked):
    print("%s %s (%0.2f%%) staked" % (
        c18(staked),
        token,
        (staked / total) * 100
    ))

print("\n------ Claim Stats ------")
show_claim_stats("Total Claims", OPTIONAL_FUNDING + MANDATORY_FUNDING, ogv.balanceOf(OPTIONAL) + ogv.balanceOf(MANDATORY))
show_claim_stats("From OUSD, required lockup", MANDATORY_FUNDING, ogv.balanceOf(MANDATORY))
show_claim_stats("From OGN, optional lockup", OPTIONAL_FUNDING, ogv.balanceOf(OPTIONAL))
print("\n------ Staking Stats ------")
show_staking_stats("OGV", ogv.totalSupply(), ogv.balanceOf(OGV_STAKING))
print("\n")
