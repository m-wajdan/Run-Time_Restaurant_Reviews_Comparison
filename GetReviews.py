from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def DataScrapping(base_url, ReviewsReq):

    driver = webdriver.Chrome()


    Reviews = {
        "Name": [],
        "Review": [],
        "OverAll": [],
        "Food": [],
        "Service": [],
        "Ambience": [],
        "Date": []  
    }

    currentPage = 1
    reviews_scraped = 0

    while reviews_scraped < ReviewsReq:
        page_url = f"{base_url}?page={currentPage}"
        driver.get(page_url)

        try:
            waitTime = WebDriverWait(driver, 5)
            waitTime.until(EC.presence_of_element_located((By.XPATH, "//*[@id='restProfileReviewsContent']")))

            for i in range(1, 11):
                if reviews_scraped >= ReviewsReq:
                    break

                try:
                    name = driver.find_element(By.XPATH, f'//*[@id="restProfileReviewsContent"]/li[{i}]/section/p[1]').text
                    review = driver.find_element(By.XPATH, f'//*[@id="restProfileReviewsContent"]/li[{i}]/div/div[2]/span[1]').text
                    overall = driver.find_element(By.XPATH, f'//*[@id="restProfileReviewsContent"]/li[{i}]/div/ol/li[1]/span').text
                    food = driver.find_element(By.XPATH, f'//*[@id="restProfileReviewsContent"]/li[{i}]/div/ol/li[2]/span').text
                    service = driver.find_element(By.XPATH, f'//*[@id="restProfileReviewsContent"]/li[{i}]/div/ol/li[3]/span').text
                    ambience = driver.find_element(By.XPATH, f'//*[@id="restProfileReviewsContent"]/li[{i}]/div/ol/li[4]/span').text
                    date = driver.find_element(By.XPATH, f'//*[@id="restProfileReviewsContent"]/li[{i}]/div/div[1]/p').text  

                    Reviews['Name'].append(name)
                    Reviews['Review'].append(review)
                    Reviews['OverAll'].append(overall)
                    Reviews['Food'].append(food)
                    Reviews['Service'].append(service)
                    Reviews['Ambience'].append(ambience)
                    Reviews['Date'].append(date)  

                    reviews_scraped += 1

                except Exception as e:
                    print(f"Error scraping review {i} on page {currentPage}: {e}")
                    continue

        except Exception as e:
            print(f"Error loading page {currentPage}: {e}")

        WebDriverWait(driver, 10)
        currentPage += 1

    driver.quit()
    return pd.DataFrame(Reviews)
