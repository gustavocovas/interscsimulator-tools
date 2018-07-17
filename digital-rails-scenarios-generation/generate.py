import os

scenarios_root = 'digital-rails-scenarios'

if not os.path.exists(scenarios_root):
  os.makedirs(scenarios_root)

for ratio in range (0, 101, 5):
  scenario_name = 'peak_dr_algo_1_' + str(ratio)
  print('Generating {}'.format(scenario_name))

  scenario_path = scenarios_root + '/' + scenario_name
  if not os.path.exists(scenario_path):
    os.makedirs(scenario_path)

  os.system("python ../trip-file-generation/generate.py {} > {}/trips.xml".format(ratio / 100, scenario_path))

  config_template = """
<scsimulator_config>
  <config 
    trip_file="../{scenario_path}/trips.xml" 
    map_file="../{scenarios_root}/network.xml" 
    output_file="../{scenario_path}/events.xml" 
    traffic_signals_file="../{scenarios_root}/signals.xml"
    simulation_time="86400"/>
</scsimulator_config>
"""
  context = {"scenarios_root": scenarios_root, "scenario_path": scenario_path} 

  with open('{}/config.xml'.format(scenario_path),'w') as f:
    f.write(config_template.format(**context))
