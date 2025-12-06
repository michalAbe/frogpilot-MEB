from selfdrive.car.volkswagen.vwcan import create_meb_steering_control, create_meb_acc_control

class CarController:
  def __init__(self, dbc_name, CP, VM):
    self.apply_steer_last = 0
    self.frame = 0

  def update(self, CC, CS):
    can_sends = []

    if CC.enabled:
      apply_steer = CC.actuators.steer
      can_sends.append(create_meb_steering_control(apply_steer, CC.enabled))

      if CC.longActive:
        can_sends.append(create_meb_acc_control(CC.actuators, CS, CC.enabled))

    return can_sends
