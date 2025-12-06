from selfdrive.car import STD_CARGO_KG
from selfdrive.car.interfaces import CarInterfaceBase

class CarInterface(CarInterfaceBase):
  @staticmethod
  def get_params(candidate, fingerprint=None, car_fw=None, experimental_long=False):
    ret = CarInterfaceBase.get_std_params(candidate, fingerprint)
    ret.carName = "volkswagen"
    ret.safetyConfigs = [CarInterfaceBase.get_torque_safety_config(0x712)]  # MEB EPS
    ret.steerActuatorDelay = 0.12
    ret.steerLimitTimer = 0.8
    ret.steerRatio = 14.8
    ret.mass = 1900 + STD_CARGO_KG
    ret.wheelbase = 2.765
    ret.centerToFront = ret.wheelbase * 0.44
    ret.minEnableSpeed = -1.
    ret.radarOffCan = True
    ret.openpilotLongitudinalControl = True
    ret.enableGasInterceptor = True
    return ret
