import httpx


url_full = 'https://restcountries.com/v3.1/name/{}?fullText=true'
url_all = 'https://restcountries.com/v3.1/all'


# Head class
class Country:
	# Init function
	def __init__(self, name: str) -> None:
		self.name = name
		self.response = httpx.get(url_full.format(self.name)).json()

	# Return Different types of the country name
	def country_name(self, common_name=True, official_name=False, short_name=False):
		# Store the country name
		list_: list = []

		# If common name is True
		if common_name:
			list_.append((self.response[0]['name']['common']))

		# If official name is True
		if official_name:
			list_.append((self.response[0]['name']['official']))

		# If short name is True
		if short_name:
			list_.append((self.response[0]['altSpellings'][0]))

		# Else nothing given
		if len(list_) == 0:
			return None

		# Return the information
		return tuple(i for i in list_)

	# Reply answers for is... questions
	def is_(self, independent=True, landlocked=False, un_member=False):
		# Answer collection
		list_ = []

		# Check for is independent
		if independent:
			list_.append(self.response[0]['independent'])

		# Check for is landlocked
		if landlocked:
			list_.append(self.response[0]['landlocked'])

		# Check for is United Nation's member
		if un_member:
			list_.append(self.response[0]['unMember'])

		# Return if nothing chosen
		if len(list_) == 0:
			return None

		# Return the answer
		return tuple(i for i in list_)

	# Currency information of the country
	def currency(self, currency=True, name=False, symbol=False):
		# Answer collection
		list_ = []

		# Show short name of the currency
		if currency:
			for i in self.response[0]['currencies'].keys():
				list_.append(i)

		# Show name of the currency
		if name:
			for i in self.response[0]['currencies'].values():
				list_.append(i['name'])

		# Show symbol of the currency
		if symbol:
			for i in self.response[0]['currencies'].values():
				list_.append(i['symbol'])

		# Return None if no currency information
		if len(list_) == 0:
			return None

		# Return the answer
		return tuple(i for i in list_)

	# Phone number of the country
	def phone(self, root=True, suffix=False):
		# Answer collector
		list_ = []

		# Show root of the phone
		if root:
			list_.append(self.response[0]['idd']['root'])

		# Show suffix of the phone
		if suffix:
			list_.append([i for i in self.response[0]['idd']['suffixes']])

		# Return None if no answer
		if len(list_) == 0:
			return None

		# Return the answer
		return tuple(i for i in list_)

	# Language of the country
	def language(self):
		# Answer collector
		list_ = []

		# Get the answer
		for i in self.response[0]['languages'].values():
			list_.append(i)

		# Return the answer
		return tuple(i for i in list_)

	# Map of the country
	def map(self, g_map=True, borders=False):
		# Answer collector
		list_ = []

		# Google maps
		if g_map:
			list_.append(self.response[0]['maps']['googleMaps'])

		# Borders of the country
		if borders:
			for i in self.response[0]['borders']:
				for j in httpx.get(url_all).json():
					if j['cca3'] == i.upper():
						name = j['name']['common']
						dict_ = {i: name}
						list_.append(dict_)

		# Return none if there are no infos asked
		if len(list_) == 0:
			return None

		# Return answer
		return tuple(i for i in list_)

	# Domain name of the country
	def domain_name(self):
		# Answer collector
		list_ = []
		list_.append(self.response[0]['tld'][0])

		return tuple(i for i in list_)

	# Capital city of the country
	def capital_city(self):
		return tuple(i for i in self.response[0]['capital'])

	# Flag of the country
	def flag(self):
		return (self.response[0]['flags']['png'],)

	# Car number of the country
	def car(self, signs=True, side=False):
		list_ = []

		if signs:
			list_.append([i for i in self.response[0]['car']['signs']][0])

		if side:
			list_.append(self.response[0]['car']['side'])

		if len(list_) == 0:
			return None

		return tuple(i for i in list_)

	# Time zone of the country
	def time_zone(self):
		return tuple(i for i in self.response[0]['timezones'])

	# Continent of the country
	def continent(self, continent=True, sub_continent=False):
		list_ = []

		if continent:
			list_.append(self.response[0]['region'])

		if sub_continent:
			list_.append(self.response[0]['subregion'])

		if len(list_) == 0:
			return None

		return tuple(i for i in list_)

	# Coat of arm of the country
	def coat_of_arm(self):
		return (self.response[0]['coatOfArms']['png'],)

	# Start of week in the country
	def start_of_week(self):
		return (self.response[0]['startOfWeek'],)

	def all_info(self, common_name=True, official_name=False, short_name=False, phone=False, border=False,
				 landlocked=False, independent=False, un_member=False, continent=False, time_zone=False, flag=False,
				 currency=False, currency_symbol=False, currency_name=False, capital=False, start_of_week=False,
				 coat_of_arm=False, car_sign=False, all=False):

		list_ = []
		if all:
			common_name = True
			official_name = True
			short_name = True
			phone = True
			border = True
			landlocked = True
			independent = True
			un_member = True
			continent = True
			time_zone = True
			flag = True
			currency = True
			currency_symbol = True
			currency_name = True
			capital = True
			start_of_week = True
			coat_of_arm = True
			car_sign = True

			if common_name:
				list_.append(self.country_name())

			if official_name:
				list_.append(self.country_name(common_name=False, official_name=True))

			if short_name:
				list_.append(self.country_name(common_name=False, short_name=True))

			if phone:
				list_.append(self.phone(suffix=True))

			if border:
				list_.append(self.map(g_map=False, borders=True))

			if landlocked:
				list_.append(self.is_(independent=False, landlocked=True))

			if independent:
				list_.append(self.is_())

			if un_member:
				list_.append(self.is_(independent=False, un_member=True))

			if continent:
				list_.append(self.continent())

			if time_zone:
				list_.append(self.time_zone())

			if flag:
				list_.append(self.flag)

			if currency:
				list_.append(self.currency())

			if currency_symbol:
				list_.append(self.currency(currency=False, symbol=True))

			if currency_name:
				list_.append(self.currency(currency=False, name=True))

			if capital:
				list_.append(self.capital_city())

			if start_of_week:
				list_.append(self.start_of_week())

			if coat_of_arm:
				list_.append(self.coat_of_arm())

			if car_sign:
				list_.append(self.car())

			return tuple(i for i in list_)

		if common_name:
			list_.append(self.country_name())

		if official_name:
			list_.append(self.country_name(common_name=False, official_name=True))

		if short_name:
			list_.append(self.country_name(common_name=False, short_name=True))

		if phone:
			list_.append(self.phone(suffix=True))

		if border:
			list_.append(self.map(g_map=False, borders=True))

		if landlocked:
			list_.append(self.is_(independent=False, landlocked=True))

		if independent:
			list_.append(self.is_())

		if un_member:
			list_.append(self.is_(independent=False, un_member=True))

		if continent:
			list_.append(self.continent())

		if time_zone:
			list_.append(self.time_zone())

		if flag:
			list_.append(self.flag)

		if currency:
			list_.append(self.currency())

		if currency_symbol:
			list_.append(self.currency(currency=False, symbol=True))

		if currency_name:
			list_.append(self.currency(currency=False, name=True))

		if capital:
			list_.append(self.capital_city())

		if start_of_week:
			list_.append(self.start_of_week())

		if coat_of_arm:
			list_.append(self.coat_of_arm())

		if car_sign:
			list_.append(self.car())

		return tuple(i for i in list_)

