class OpenFile:
  """Context Manger to open a file"""
  def __init__(self, fileName, mode):
    """Initializes the file object"""
    # self.fileName = fileName
    # self.mode = mode
    # self.f = None
    self.f = open(fileName, mode)

  def __enter__(self):
    """Returns the file object"""
    return self.f

  def __exit__(self, exc_type, exc_value, exc_trace):
    """Closes the file object"""
    self.f.close()


with OpenFile("test1.txt","w") as f:
   f.write("Test 1")
print("testing complete!")