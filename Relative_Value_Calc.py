from Terran_Cannon import StatsTerranCannon as TC


class RelativeValueCalc:
    def __init__(self):
        self._PowerPerP = float(input("Power per P:"))
        self._TC = TC()

    def calculate_relative(self):
        print("Input in order:")
        user_input = input("P Cost, Damage, Rounds Per Second, Range, Muzzle Velocity, Power Cost:\n").split()
        for i in range(len(user_input)):
            user_input[i] = user_input[i].strip(',')
        sliced = user_input
        points = int(sliced[0])
        damage = float(sliced[1])
        rps = float(sliced[2])
        weapon_range = float(sliced[3])
        mvel = float(sliced[4])
        power = float(sliced[5])

        out_string = "|"
        p_cost = points + ((power * rps) / self._PowerPerP)
        relative_p_cost = round(p_cost / self._TC.Points, 2)
        out_string += str(relative_p_cost) + "x P cost|"
        relative_damage = round((damage * rps) / (self._TC.Damage * self._TC.RPS), 2)
        out_string += str(relative_damage) + "x Damage|"
        relative_fire_rate = round(rps / self._TC.RPS, 2)
        out_string += str(relative_fire_rate) + "x Fire Rate|"
        relative_range = round(weapon_range / self._TC.Range, 2)
        out_string += str(relative_range) + "x Range|"
        relative_velocity = round(mvel / self._TC.MVel, 2)
        out_string += str(relative_velocity) + "x Muzzle Velocity|"
        relative_power = round(((power / self._PowerPerP) * rps) / ((self._TC.Power * self._TC.RPS) / 3.33), 2)
        out_string += str(relative_power) + "x Power P Contribution|"
        relative_value = round(self.relative_average(work_list=[relative_damage, relative_fire_rate, relative_range,
                                                                relative_velocity, relative_power]), 2)
        out_string += str(relative_value) + "x the worth of a Terran Plasma Cannon for " + str(relative_p_cost) + "x the cost.|"
        print(out_string)

    @staticmethod
    def relative_average(work_list: list) -> float:
        total = 0
        for item in work_list:
            total += item
        total /= len(work_list)
        return total
