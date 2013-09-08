import feeds

feed = feeds.fc

reader_class = feeds.MESSAGE_TYPES[feed['message_type']]
reader = reader_class(feed['messages'])
reader.decode_packet("ADIS\x00\x00\x00\x00\x00\x00\x00\x18\x2D\x08\x06\x00\x04\x00\xF7\xFF\x28\x01\x01\x00\x00\x00\x9F\x04\x8D\xFF\xC8\xFD\x3C\x00\x00\x00ROLL\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x01")
