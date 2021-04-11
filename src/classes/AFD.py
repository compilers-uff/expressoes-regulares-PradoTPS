class AFD:
  def __init__(self):
    super().__init__()

  def accepted(self, word):
    return True

  @staticmethod
  def afnToAFD(er):
    return AFD()

  @staticmethod
  def afdToAFDmin(afd):
    return afd