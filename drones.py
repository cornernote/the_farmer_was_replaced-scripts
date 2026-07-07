def process_tasks(tasks, wait = False):
	activeDrones = []
	results = {}

	for task in tasks:
		if not 'id' in task:
			task['id'] = random()

		drone = spawn_drone(task['method'], task['param'])
		if drone:
			activeDrones.append({'id': task['id'], 'drone': drone})
		else:
			results[task['id']] = task['method'](task['param'])

	if wait:
		for active in activeDrones:
			results[active['id']] = wait_for(active['drone'])

	return results