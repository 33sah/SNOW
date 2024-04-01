import subprocess
import itertools

# Indexing Magic
def seq(start, end, step):
    if step == 0:
        raise ValueError("step must not be 0")
    sample_count = int(abs(end - start) / step)
    return itertools.islice(itertools.count(start, step), sample_count)

# Changing run.mac file for correct shape / energy
def texteditor(shape, Energy, linenumbers):
    if all(type(x) in [int] for x in linenumbers):
    # Checking if integers passed in argument

        with open("run.mac", "r") as file:
            text = file.read()
    
        lines = text.split("\n")
        lines[linenumbers[0]] = f"/geometry/source {shape}.tg"
        lines[linenumbers[1]] = f"/gps/energy {Energy} GeV"
        FileEnergy = str(Energy).replace(".","_")
        # Defining standard deviation of gaussian energy, +/- 1% are roughly bounds so dividing by 3 (99.7% of points in range) gives us the value of sigma to 3 d.p
        Sigma = round(((Energy * 0.01)/3),3)
        lines[linenumbers[2]] = f"/gps/ene/sigma {Sigma} GeV"
        lines[linenumbers[3]] = f"/analysis/setFileName results{FileEnergy}{shape}.root"
        final_text = "\n".join(lines)
    
        with open("run.mac", "w") as file:
            file.write(final_text)

def main():
  # These are the names of geometry files
  shapes = ["cyl","sph","tor"]

  # Run run.mac with gears
  command = "gears.exe run.mac"

  # Line Numbers to change - Geometry, Energy Range + Distribution and Data - Remember these will be 1 smaller than actuality due to Python list starting at index = 0
  Numbers = [5,34,35,41]
  
  for shape in shapes:
      for x in seq(0.1,5.1,0.1):
          # Python rounding error
          texteditor(shape, round(x,2), Numbers)
          subprocess.run(command, shell=True)
          # Run command

if __name__ == "__main__":
  main()

    
