from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 目标URL
url = 'https://space.coze.cn/web?uri=7516483041917992986%2F%E6%97%A0%E4%BA%BA%E6%9C%BAmotor%E5%B7%A5%E5%8E%82%E5%BB%BA%E8%AE%BE%E6%8A%A5%E5%91%8A-04985417dd.html'

# 配置Chrome选项
chrome_options = Options()
chrome_options.add_argument('--headless=new')  # 无头模式
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1')

try:
    # 初始化WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    # 等待页面加载完成（最多等待15秒）
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )
    
    # 等待动态内容加载
    time.sleep(5)
    
    # 截取页面截图用于诊断
    driver.save_screenshot('page_screenshot.png')
    
    # 获取页面源码
    page_source = driver.page_source
    with open('page_source.html', 'w', encoding='utf-8') as f:
        f.write(page_source)
    
    # 处理iframe内容
    # 检查iframe是否存在
    try:
        iframe_elements = driver.find_elements(By.TAG_NAME, 'iframe')
        print(f'找到 {len(iframe_elements)} 个iframe元素')
        if len(iframe_elements) == 0:
            raise Exception('未找到任何iframe元素')
        iframe = iframe_elements[0]
        print('找到iframe元素，准备切换')
    except Exception as e:
        content_text = f'查找iframe失败: {str(e)}'
        page_text = driver.find_element(By.TAG_NAME, 'body').text
        # 保存错误日志
        with open('iframe_error.log', 'w', encoding='utf-8') as f:
            f.write(f'查找iframe失败: {str(e)}')
    else:
        try:
            # 切换到iframe
            driver.switch_to.frame(iframe)
            print('已切换到iframe')
            
            # 在iframe中等待内容加载
            WebDriverWait(driver, 20).until(
                lambda d: len(d.find_element(By.TAG_NAME, 'body').text.strip()) > 0 or 
                          len(d.page_source) > 1000
            )
            print('iframe内容加载完成')
            
            # 获取iframe源码
            iframe_source = driver.page_source
            with open('iframe_source.html', 'w', encoding='utf-8') as f:
                f.write(iframe_source)
            
            # 在iframe中尝试获取内容
            iframe_body = driver.find_element(By.TAG_NAME, 'body')
            iframe_text = iframe_body.text
            
            # 保存iframe内容
            with open('iframe_content.txt', 'w', encoding='utf-8') as f:
                f.write(iframe_text)
            
            # 尝试多种常见内容选择器
            selectors = ['div.content', 'div.main', 'article', 'div.container', 'div#content', 'div.doc-content', 'div.article-content']
            content_text = '未能找到特定内容区域'
            for selector in selectors:
                try:
                    content_element = driver.find_element(By.CSS_SELECTOR, selector)
                    element_text = content_element.text.strip()
                    if len(element_text) > 0:
                        content_text = f'使用选择器 {selector} 找到内容: {element_text[:200]}...'
                        break
                except:
                    continue
            
            # 检查是否有嵌套iframe
            try:
                nested_iframe = driver.find_element(By.TAG_NAME, 'iframe')
                content_text += '; 发现嵌套iframe'
            except:
                pass
            
            # 获取页面文本内容
            page_text = iframe_text
            
            # 输出iframe诊断信息
            print(f'iframe源码大小: {len(iframe_source)} 字符')
            print(f'iframe文本长度: {len(iframe_text)} 字符')
            
            # 切回主文档
            driver.switch_to.default_content()
        except Exception as e:
            # 捕获详细异常信息
            import traceback
            error_details = traceback.format_exc()
            content_text = f'处理iframe时出错: {str(e)}\n详细错误:\n{error_details}'
            # 保存错误日志到文件
            with open('iframe_error.log', 'w', encoding='utf-8') as f:
                f.write(error_details)
            page_text = driver.find_element(By.TAG_NAME, 'body').text
            # 确保切回主文档
            driver.switch_to.default_content()
    
    
    # 保存内容到文件
    with open('crawled_content.txt', 'w', encoding='utf-8') as f:
        f.write(f'页面标题: {driver.title}\n\n')
        f.write(f'特定内容区域: {content_text}\n\n')
        f.write(f'完整页面文本:\n{page_text}')
    
    # 输出详细诊断信息
    print(f'页面标题: {driver.title}')
    print(f'页面源码大小: {len(page_source)} 字符')
    print(f'获取到的文本长度: {len(page_text)} 字符')
    print(f'特定内容区域状态: {content_text}')
    print('动态网页内容爬取完成，已保存到 crawled_content.txt、page_source.html 和 page_screenshot.png')
    
except Exception as e:
    print(f'爬取失败: {e}')
finally:
    # 确保浏览器关闭
    if 'driver' in locals():
        driver.quit()