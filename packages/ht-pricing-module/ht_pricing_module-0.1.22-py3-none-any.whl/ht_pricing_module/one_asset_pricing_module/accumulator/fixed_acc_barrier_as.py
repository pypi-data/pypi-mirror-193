from ..one_asset_option_base import *
from ..vanilla import Vanilla
from ..binary import Binary


class FixedAccBarrier(OneAssetOptionBase):

    def __calculate_present_value__(self) -> float:
        rst = 0

        leveraged_vanilla_option_type = {OptionType.ACCUMULATOR: OptionType.PUT,
                               OptionType.DECUMULATOR: OptionType.CALL}[self.param.option_type]
        binary_option_type = {OptionType.ACCUMULATOR: OptionType.CALL,
                              OptionType.DECUMULATOR: OptionType.PUT}[self.param.option_type]

        for obs in self.param.obs_date:
            param = Struct({})
            param['option_type'] = leveraged_vanilla_option_type
            param['exercise_type'] = self.param.exercise_type
            param['spot_price'] = self.param.spot_price
            param['strike_price'] = self.param.strike_price
            param['expiry_date'] = obs.obs_index
            param['current_date'] = self.param.current_date
            param['volatility'] = self.param.volatility
            param['riskfree_rate'] = self.param.riskfree_rate
            param['dividend'] = self.param.dividend
            param['year_base'] = int(self.param.year_base)
            leveraged_vanilla = Vanilla(param)

            param = Struct({})
            param['option_type'] = binary_option_type
            param['exercise_type'] = self.param.exercise_type
            param['spot_price'] = self.param.spot_price
            param['strike_price'] = self.param.strike_price
            param['expiry_date'] = obs.obs_index
            param['current_date'] = self.param.current_date
            param['volatility'] = self.param.volatility
            param['riskfree_rate'] = self.param.riskfree_rate
            param['dividend'] = self.param.dividend
            param['payoff'] = self.param.payoff
            param['year_base'] = int(self.param.year_base)
            binary1 = Binary(param)

            param = Struct({})
            param['option_type'] = binary_option_type
            param['exercise_type'] = self.param.exercise_type
            param['spot_price'] = self.param.spot_price
            param['strike_price'] = self.param.barrier_price
            param['expiry_date'] = obs.obs_index
            param['current_date'] = self.param.current_date
            param['volatility'] = self.param.volatility
            param['riskfree_rate'] = self.param.riskfree_rate
            param['dividend'] = self.param.dividend
            param['payoff'] = self.param.payoff
            param['year_base'] = int(self.param.year_base)
            binary2 = Binary(param)
            rst = rst + (-self.param.leverage * leveraged_vanilla.present_value()
                         + binary1.present_value()
                         - binary2.present_value())
        return rst
