#-*-coding:utf-8-*-
import enum

class SwitchInput(enum.IntEnum):
    SWITCH_OPEN  = 0  # IntEnum을 상속받아야 enum의 멤버가 int type을 갖는다.
    SWITCH_CLOSE = 1