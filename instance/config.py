# Configuration variables for our API

import os

class Config(object):
	# Parent configuration class
	DEBUG = False

class Development(Config):
	# Development environment configurations
	DEBUG = True

class Testing(Config):
	# Testing environment configurations
	DEBUG = True
	TESTING = True

class Production(Config):
	# Production environment configurations
	DEBUG = False
	TESTING = False

app_config = {
	"development": Development,
	"testing": Testing,
	"production": Production
}
