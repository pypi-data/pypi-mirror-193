import os, time

r, w = os.pipe()
  
# The returned file descriptor r and w
# can be used for reading and
# writing respectively.
  
# We will create a child process
# and using these file descriptor
# the parent process will write 
# some text and child process will
# read the text written by the parent process
  
# Create a child process
pid = os.fork()
  
# pid greater than 0 represents
# the parent process
if pid > 0:
  
    # This is the parent process 
    # Closes file descriptor r
    os.close(r)
    time.sleep(2)
    # Write some text to file descriptor w 
    print("Parent process is writing")
    text = b"Hello child process"
    os.write(w, text)
    print("Written text:", text.decode())
  
      
else:
  
    # This is the parent process 
    # Closes file descriptor w
    os.close(w)
  
    # Read the text written by parent process
    print("\nChild Process is reading")
    r = os.fdopen(r)
    print("Read text:", r.read())