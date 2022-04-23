first_name = 'Yao'
last_name = 'Xiong'
full_name = first_name + " " + last_name
print(full_name)

height_in_inches = 66
print(
  "height_in_inches: ", height_in_inches,
  "type: ",type(height_in_inches)
)

height_in_inches_float = float(height_in_inches)
print(
  "height_in_inches_float: ", height_in_inches_float,
  "type: ",type(height_in_inches_float)
)

height_in_meters = height_in_inches_float
print("height_in_meters:", height_in_meters)

eats_plants = True
eats_animals = False

is_animal = eats_plants or eats_animals
is_omnivore = eats_plants & eats_animals
is_plant = not is_animal
print(
  "is_animal:",is_animal,
  "is_omnivore:",is_omnivore,
  "is_plant:",is_plant,
)

mean_height_in_meters = 1.7155
short_threshold_in_meters = 1.576
tall_threshold_in_meters = 1.860

is_mean_height = height_in_meters = mean_height_in_meters
is_short = height_in_meters < short_threshold_in_meters
is_tall = height_in_meters >= tall_threshold_in_meters
is_normal_height = short_threshold_in_meters <= height_in_meters < tall_threshold_in_meters
print(
  "is_mean_height:",is_mean_height,
  "is_short:",is_short,
  "is_tall:",is_tall,
  "is_normal_height",is_normal_height,
)

nothing = None
print(
  "nothing:",nothing,
  "type:",type(nothing)
)


#===========================
#output:
#cd /home/dev/ds-py-0422-code-solutions ; /usr/bin/env /bin/python3.10 /home/dev/.vscode-server/extensions/ms-python.python-2022.4.1/pythonFiles/lib/python/debugpy/launcher 33813 -- /home/dev/ds-py-0422-code-solutions/ds-prep-python-variables/main.py
#Yao Xiong
#height_in_inches:  66 type:  <class 'int'>
#height_in_inches_float:  66.0 type:  <class 'float'>
#height_in_meters: 66.0
#is_animal: True is_omnivore: False is_plant: False
#is_mean_height: 1.7155 is_short: False is_tall: False is_normal_height True
#nothing: None type: <class 'NoneType'>
#===========================
