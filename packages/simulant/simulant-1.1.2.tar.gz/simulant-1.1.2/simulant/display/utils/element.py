import cv2
import numpy as np


def find_element(template_img_path, screenshot_img, threshold=.8):
    # Load the template image to search for
    template_img = cv2.imread(template_img_path)
    # Perform matchTemplate to get the matching result
    result = cv2.matchTemplate(screenshot_img, template_img, cv2.TM_CCOEFF_NORMED)
    # Set the threshold for finding matches
    matches = np.where(result >= threshold)
    # Create an empty list to store the coordinates of matches
    coords = []
    for match in zip(*matches[::-1]):
        coords.append((match[0], match[1], match[0] + template_img.shape[1], match[1] + template_img.shape[0]))
    if coords:
        return coords[0][:2], coords[0][2:]
    return


def find_elements(template_img_path, screenshot_img, threshold=.8):
    # screenshot_img = cv2.imread(screanshot_img_path)
    # Load the template image to search for
    template_img = cv2.imread(template_img_path)
    # Perform matchTemplate to get the matching result
    result = cv2.matchTemplate(screenshot_img, template_img, cv2.TM_CCOEFF_NORMED)
    # Find all the matches in the screenshot
    matches = np.where(result >= threshold)
    # Store the coordinates of all the matches in an array
    coordinates = np.column_stack((matches[1], matches[0]))
    return coordinates
