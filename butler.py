import asyncio

async def hire_butler(loop = asyncio.get_event_loop()):
	await asyncio.sleep(10)

if __name__ == '__main__':
	
	#print the README file at the start of the server:.codename butler

	with open('README', 'r') as fd:
		readme = fd.read()
		print(readme)
	
	main_loop = asyncio.get_event_loop()
	# deploy butler in a given loop ~> current by default
	try:
		main_loop.run_until_complete(hire_butler())
		
	except KeyboardInterrupt as e:
		main_loop.stop()
