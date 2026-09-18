def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	if newValue.value: 
		logger = system.util.logger('Tag') 
		logger.info('tag changed') 