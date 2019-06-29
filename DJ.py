import os
import random
import time

myarray = []
time_limit_arr = []
i = 0
time_count = 0
f = open('record.txt', 'w')
f2 = open('party_list.txt', 'w')
class DJ():
	def __init__(self, name, relation, song, time_count):
		extra = 0
		self.name = name
		self.relation = relation
		self.song = song
		self.time_log = time_count
		if time_count == 0:
			self.time_limit = random.randrange(15,30)
			time_limit_arr.append(self.time_limit)
			print(f'{time_count} Playing- {song} {time_limit_arr[-1]}')
			f.write(f'{time_count} Playing- {song} {time_limit_arr[-1]}')
		

	def request_friend(self, name, value, song, time_log):
		limit = random.randrange(15,30)
		if value == 'friend':
			print(time_log,'-', name,'request', value, song, limit)
			f.write(f'\n{time_log} - {name}, request , {value}, {song}, {limit}')
			
			self.pause(time_log, True, song, limit)
			time_limit_arr.append(limit)
			
		else:
			print(time_log,'-', name,'request', value, song, limit)
			f.write(f'\n{time_log} - {name},request, {value}, {song}, {limit}')
			time_log += (time_limit_arr[-1]-5)
			
			time_limit_arr.append(limit)
			self.pause(time_log, False, song, limit)
			

	def pause(self, time_log, binary, song, limit):
		if binary == True:
			print(time_log, '-', self.name,'song paused',self.relation, self.song)
			f.write(f'\n{time_log} - {self.name}, song paused ,{self.relation}, {self.song}')
			print(f'{time_log} Playing- {song}')
			f.write(f'\n{time_log} Playing- {song}')
			myarray.append(time_log)

		else:
			print(time_log, '-', self.name,'song paused',self.relation, self.song)
			f.write(f'\n{time_log} - {self.name}, song paused ,{self.relation}, {self.song}')
			print(f'{time_log} Playing- {song}')
			f.write(f'\n{time_log} Playing- {song}')
			myarray.append(time_log)

# Dictionary of party-goers

people = {'Nick':{'relation':'friend', 'song': 'Bring it on Home'}, 'Peter':{'relation':'enemy', 'song': 
'Hey Ya'}, 'Max':{'relation':'enemy', 'song': 'Better Believe it Now'}, 'Emmy':{'relation':'friend', 'song': 'California Girls'},
'Supreya':{'relation':'acquaintance', 'song': 'Overflow'},'Marally':{'relation':'enemy', 'song': 'Turkish Dance'},
'Jake':{'relation':'acquaintance', 'song': 'Get Jiggy With it'},
'Ashu':{'relation':'friend', 'song': 'U & I'},}



# Uncomment the code block below to enter your own participants

# people = {}
# print('DJ Master! party entry, press q to quit or enter to keep going\n')
# while input(' ') != 'q':
# 	name = input('Insert name of person\n ')
# 	relation = input('Insert relation of person to DJ\n ')
# 	song = input('Insert song of choice\n ')
# 	people[name] = {'relation': relation, 'song': song}


# Write header of participant list file

f2.write(f'Name|  Relation  | Song | Time Limit\n')

# Loop that iterates over the participant list and interacts with the DJ class


for key,value in people.items():
	
	
	name = key
	relation = value['relation']
	song = value['song']
	
	
	if time_count == 0:
		dj = DJ(name,value['relation'],value['song'],time_count)
		time_count += 5
		
	else:
		
		if value['relation'] == 'friend':
			i+=1
			if len(myarray)>0:
				time_count = myarray[-1]+5

			dj.request_friend(name, value['relation'], value['song'], time_count)
			dj = DJ(name,value['relation'],value['song'],time_count)
			time_count += 5

			if i == len(people)-1:
				total_time_counted = myarray[-1]+time_limit_arr[-1]
		
				if total_time_counted > 60:
					print(f'\nDJ finished, Total: {int(total_time_counted/60)} minutes and {total_time_counted%60} seconds')
					f.write(f'\nDJ finished, Total: {int(total_time_counted/60)} minutes and {total_time_counted%60} seconds')
					f.close()
				
				else:
					print(f'\nDJ finished, Total Seconds: {total_time_counted}')
					f.write(f'\nDJ finished, Total Seconds: {total_time_counted}')
					f.close()
					

		if value['relation'] != 'friend':
			i+=1
			if len(myarray)>0:
				time_count = myarray[-1]+5
			
			dj_call = dj.request_friend(name, value['relation'], value['song'], time_count)
			dj = DJ(name,value['relation'],value['song'],time_count)
			time_count += 5
	
			if i == len(people)-1:
				total_time_counted = myarray[-1]+time_limit_arr[-1]
				if total_time_counted > 60:
					print(f'\nDJ finished, Total: {int(total_time_counted/60)} minutes and {total_time_counted%60} seconds')
					f.write(f'\nDJ finished, Total: {int(total_time_counted/60)} minutes and {total_time_counted%60} seconds')
					f.close()
					
				else:
					print(f'\nDJ finished, Total Seconds: {total_time_counted}')
					f.write(f'\nDJ finished, Total Seconds: {total_time_counted}')
					f.close()
					
	if len(time_limit_arr) > 0:
		time_limit_val = time_limit_arr[-1]
	else:
		time_limit_val = time_limit_arr[0]

	
	f2.write(f'\n{key}, {relation},  {song},  (time limit: {time_limit_val} sec) ')
	
	

# 'Supreya':'friend', 'Alex':'acquaintance', 'Marally':'acquaintance', 'Max':'friend', 'Emmy': 'enemy'}