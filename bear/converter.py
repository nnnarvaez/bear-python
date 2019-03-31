import math

from .amount import Amount
from .instance import shared_beard_instance


class Converter(object):
    """ Converter simplifies the handling of different metrics of
        the blockchain

        :param Beard beard_instance: Beard() instance to
        use when accessing a RPC

    """

    def __init__(self, beard_instance=None):
        self.beard = beard_instance or shared_beard_instance()

        self.CONTENT_CONSTANT = 2000000000000

    def bsd_median_price(self):
        """ Obtain the bsd price as derived from the median over all
            witness feeds. Return value will be BSD
        """
        return (Amount(self.beard.get_feed_history()['current_median_history']
                       ['base']).amount / Amount(self.beard.get_feed_history(
        )['current_median_history']['quote']).amount)

    def bear_per_mvests(self):
        """ Obtain BEARS/MVESTS ratio
        """
        info = self.beard.get_dynamic_global_properties()
        return (Amount(info["total_coining_fund_bears"]).amount /
                (Amount(info["total_coining_shares"]).amount / 1e6))

    def vests_to_sp(self, vests):
        """ Obtain SP from VESTS (not MVESTS!)

            :param number vests: Vests to convert to SP
        """
        return vests / 1e6 * self.bear_per_mvests()

    def sp_to_vests(self, sp):
        """ Obtain VESTS (not MVESTS!) from SP

            :param number sp: SP to convert
        """
        return sp * 1e6 / self.bear_per_mvests()

    def sp_to_rshares(self, sp, voting_power=10000, vote_pct=10000):
        """ Obtain the r-shares

            :param number sp: Bear Power
            :param int voting_power: voting power (100% = 10000)
            :param int vote_pct: voting participation (100% = 10000)
        """
        # calculate our account voting shares (from vests), mine is 6.08b
        vesting_shares = int(self.sp_to_vests(sp) * 1e6)

        # get props
        props = self.beard.get_dynamic_global_properties()

        # determine voting power used
        used_power = int((voting_power * vote_pct) / 10000);
        max_vote_denom = props['vote_power_reserve_rate'] * (5 * 60 * 60 * 24) / (60 * 60 * 24);
        used_power = int((used_power + max_vote_denom - 1) / max_vote_denom)

        # calculate vote rshares
        rshares = ((vesting_shares * used_power) / 10000)

        return rshares

    def bear_to_bsd(self, amount_bear):
        """ Conversion Ratio for given amount of BEARS to BSD at current
            price feed

            :param number amount_bear: Amount of BEARS
        """
        return self.bsd_median_price() * amount_bear

    def bsd_to_bear(self, amount_bsd):
        """ Conversion Ratio for given amount of BSD to BEARS at current
            price feed

            :param number amount_bsd: Amount of BSD
        """
        return amount_bsd / self.bsd_median_price()

    def bsd_to_rshares(self, bsd_payout):
        """ Obtain r-shares from BSD

            :param number bsd_payout: Amount of BSD
        """
        bear_payout = self.bsd_to_bear(bsd_payout)

        props = self.beard.get_dynamic_global_properties()
        total_reward_fund_bear = Amount(props['total_reward_fund_bears'])
        total_reward_shares2 = int(props['total_reward_shares2'])

        post_rshares2 = (
                                bear_payout / total_reward_fund_bear) * total_reward_shares2

        rshares = math.sqrt(
            self.CONTENT_CONSTANT ** 2 + post_rshares2) - self.CONTENT_CONSTANT
        return rshares

    def rshares_2_weight(self, rshares):
        """ Obtain weight from rshares

            :param number rshares: R-Shares
        """
        _max = 2 ** 64 - 1
        return (_max * rshares) / (2 * self.CONTENT_CONSTANT + rshares)
