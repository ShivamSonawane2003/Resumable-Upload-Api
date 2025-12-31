#!/usr/bin/env python
"""Minimal test to check if logging works"""
import sys
import os

# Add the app directory to path
sys.path.insert(0, os.path.dirname(__file__))

print("Starting minimal logging test...")

try:
    from app.config import settings
    print(f"✓ Config loaded. LOG_FILE: {settings.LOG_FILE}")
    print(f"  Absolute path: {os.path.abspath(settings.LOG_FILE)}")
    
    # Remove old log file
    if os.path.exists(settings.LOG_FILE):
        os.remove(settings.LOG_FILE)
        print(f"  Removed old log file")
    
    from app.utils.logging_config import logger, setup_logging
    print(f"✓ Logger imported successfully")
    print(f"  Logger: {logger}")
    print(f"  Logger level: {logger.level}")
    print(f"  Logger handlers: {logger.handlers}")
    
    for i, handler in enumerate(logger.handlers):
        print(f"    Handler {i}: {handler} (level={handler.level})")
    
    # Test logging
    print(f"About to log test message...")
    logger.info("TEST MESSAGE FROM MINIMAL SCRIPT")
    print(f"✓ Logged test message")
    
    # Flush all handlers
    print(f"Flushing handlers...")
    for handler in logger.handlers:
        handler.flush()
    print(f"✓ Handlers flushed")
    
    # Check if file exists and has content
    import time
    time.sleep(1)
    
    if os.path.exists(settings.LOG_FILE):
        size = os.path.getsize(settings.LOG_FILE)
        print(f"✓ Log file exists: {settings.LOG_FILE}")
        print(f"  File size: {size} bytes")
        if size > 0:
            with open(settings.LOG_FILE, 'r') as f:
                content = f.read()
                print(f"  Content:\n{content}")
        else:
            print(f"  File is empty!")
    else:
        print(f"✗ Log file does not exist: {settings.LOG_FILE}")
        
except Exception as e:
    print(f"✗ ERROR: {e}")
    import traceback
    traceback.print_exc()

print("Test complete")

