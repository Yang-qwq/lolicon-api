# -*- coding: utf-8 -*-
import os
import sys
import tempfile
sys.path.append("..")  # Adjust the path to import the module correctly

import lolicon_api  # Import the lolicon_api module

def test_tags_transformer():
    """Test the tags_transformer function from lolicon_api module."""
    # Test 1
    tags = ["Tag1|Tag2", "Tag3|Tag4"]
    result = lolicon_api.tags_transformer(tags)
    assert result == ["tag1|tag2", "tag3|tag4"], "Tags should be transformed correctly"

    # Test 2
    tags = [["Tag1", "Tag2"], ["Tag3", "Tag4"]]
    result = lolicon_api.tags_transformer(tags)
    assert result == ["tag1|tag2", "tag3|tag4"], "Tags should be transformed correctly"

    # Test 3
    tags = [["Tag1"], ["Tag2"], ["Tag3"], ["Tag4"]]
    result = lolicon_api.tags_transformer(tags)
    assert result == ["tag1", "tag2", "tag3", "tag4"], "Tags should be transformed correctly"

    # Test with an empty list
    tags = []
    result = lolicon_api.tags_transformer(tags)
    assert result == [], "Empty tags should return an empty list"

def test_fetch():
    """Test the get function from lolicon_api module."""
    # Test with no tags and default parameters
    response = lolicon_api.fetch(r18=False, num=1)
    assert isinstance(response, dict), "Response should be a dictionary"
    assert response["error"] == "", "Error should be an empty string"

def test_download_image():
    """Test the download_image function from lolicon_api module."""
    # Assuming the first image URL is valid and accessible
    response = lolicon_api.fetch(r18=False, num=1)
    image_url = response["data"][0]["urls"]["original"]

    # Download the image to a temporary file
    temp_file = tempfile.mktemp(image_url.split("/")[-1])  # Create a temp file with the image name

    lolicon_api.download_image(image_url, save_path=temp_file)

    # Check if the file was created
    assert os.path.exists(temp_file), "Image file should be created"

    # Clean up the temporary file
    os.remove(temp_file)
