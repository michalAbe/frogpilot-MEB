from selfdrive.car import dbc_dict
from selfdrive.car.volkswagen.values import CAR, PQ_CARS, MQB_CARS, MLB_CARS, MEB_CARS, Ecu, BUTTON_STATES

def get_can_parser(CP):
  signals = [
    ("ESP_19_Bremspedal", 100),
    ("ESP_05_Radarsensor", 50),
    ("GRA_ACC_01", 50),
    ("SWA_01", 50),
    ("TSK_06", 20),
    ("HCA_01", 50),
    ("LWI_01", 20),
  ]
  checks = []
  return CANParser("vw_meb", signals, checks, 0)

class CarInterface:
  @staticmethod
  def get_params(candidate, fingerprint=None, car_fw=None):
    ret = car.CarParams.new_message()
    ret.carName = "volkswagen"
    ret.carFingerprint = "CUPRA BORN 2021"
    ret.safetyConfigs = [get_safety_config(car.CarParams.SafetyModel.volkswagen)]
    ret.steerActuatorDelay = 0.1
    ret.steerRateCost = 1.0
    ret.steerLimitTimer = 0.4
    ret.radarOffCan = True
    ret.openpilotLongitudinalControl = True
    ret.minEnableSpeed = -1.
    ret.mass = 1900
    ret.wheelbase = 2.77
    ret.steerRatio = 14.8
    return ret

CAR = CAR.CUPRA_BORN_21 = "CUPRA BORN 2021"
MEB_CARS = {CAR.CUPRA_BORN_21} 
