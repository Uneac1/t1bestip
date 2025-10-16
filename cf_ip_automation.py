import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class CFIPAutomation:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.setup_driver()
    
    def setup_driver(self):
        """设置Chrome浏览器驱动"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--disable-features=VizDisplayCompositor')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.87 Safari/537.36')
        
        # GitHub Actions环境优化
        if os.getenv('GITHUB_ACTIONS'):
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-plugins')
            chrome_options.add_argument('--disable-images')
            chrome_options.add_argument('--disable-javascript')
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, 30)
            print("Chrome浏览器驱动初始化成功")
        except Exception as e:
            print(f"Chrome浏览器驱动初始化失败: {e}")
            raise
    
    def open_website(self):
        """打开优选IP网站"""
        try:
            print("正在打开优选IP网站...")
            self.driver.get('https://t1.y130.icu/t1/bestip')
            time.sleep(3)
            print("网站加载完成")
            return True
        except Exception as e:
            print(f"打开网站失败: {e}")
            return False
    
    def clear_all_selections(self):
        """清除所有已选择的选项"""
        try:
            print("清除所有已选择的选项...")
            
            # 清除IP库选择
            ip_libraries = [
                'CF官方列表', 'CM整理列表', 'AS13335列表', 
                'AS209242列表', 'AS24429列表(Alibaba)', 
                'AS199524列表(G-Core)', '反代IP列表'
            ]
            
            for lib in ip_libraries:
                try:
                    selectors = [
                        f"//label[contains(text(), '{lib}')]/input",
                        f"//input[@value='{lib}']",
                        f"//label[contains(text(), '{lib}')]"
                    ]
                    
                    for selector in selectors:
                        try:
                            element = self.driver.find_element(By.XPATH, selector)
                            if element.is_selected():
                                element.click()
                            break
                        except:
                            continue
                except:
                    continue
            
            # 清除端口选择
            ports = ['443', '2053', '2083', '2087', '2096', '8443']
            
            for port in ports:
                try:
                    selectors = [
                        f"//label[contains(text(), '{port}')]/input",
                        f"//input[@value='{port}']",
                        f"//label[contains(text(), '{port}')]"
                    ]
                    
                    for selector in selectors:
                        try:
                            element = self.driver.find_element(By.XPATH, selector)
                            if element.is_selected():
                                element.click()
                            break
                        except:
                            continue
                except:
                    continue
            
            print("清除选择完成")
            return True
            
        except Exception as e:
            print(f"清除选择时出错: {e}")
            return False
    
    def select_cf_official(self):
        """选择CF官方列表"""
        try:
            print("正在选择CF官方列表...")
            
            selectors = [
                "//label[contains(text(), 'CF官方列表')]/input",
                "//input[@value='CF官方列表']",
                "//label[contains(text(), 'CF官方列表')]"
            ]
            
            element = None
            for selector in selectors:
                try:
                    element = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    break
                except TimeoutException:
                    continue
            
            if element:
                if element.get_attribute('type') in ['checkbox', 'radio']:
                    if not element.is_selected():
                        element.click()
                else:
                    element.click()
                print("已选择CF官方列表")
                return True
            else:
                print("未找到CF官方列表选项")
                return False
                
        except Exception as e:
            print(f"选择CF官方列表时出错: {e}")
            return False
    
    def select_port_443(self):
        """选择443端口"""
        try:
            print("正在选择443端口...")
            
            selectors = [
                "//label[contains(text(), '443')]/input",
                "//input[@value='443']",
                "//label[contains(text(), '443')]"
            ]
            
            element = None
            for selector in selectors:
                try:
                    element = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    break
                except TimeoutException:
                    continue
            
            if element:
                if element.get_attribute('type') in ['checkbox', 'radio']:
                    if not element.is_selected():
                        element.click()
                else:
                    element.click()
                print("已选择443端口")
                return True
            else:
                print("未找到443端口选项")
                return False
                
        except Exception as e:
            print(f"选择443端口时出错: {e}")
            return False
    
    def start_test(self):
        """开始延迟测试"""
        try:
            print("正在开始延迟测试...")
            
            button_selectors = [
                "//button[contains(text(), '开始延迟测试')]",
                "//input[@value='开始延迟测试']",
                "//button[contains(@class, 'start-test')]"
            ]
            
            button = None
            for selector in button_selectors:
                try:
                    button = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    break
                except TimeoutException:
                    continue
            
            if button:
                button.click()
                print("延迟测试已开始")
                return True
            else:
                print("未找到开始测试按钮")
                return False
                
        except Exception as e:
            print(f"开始测试时出错: {e}")
            return False
    
    def wait_for_test_completion(self, max_wait_time=300):
        """等待测试完成"""
        print(f"等待测试完成，最大等待时间: {max_wait_time}秒")
        
        start_time = time.time()
        while time.time() - start_time < max_wait_time:
            try:
                # 检查测试进度
                progress_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), '测试进度') or contains(text(), '完成') or contains(text(), '优选')]")
                
                if progress_elements:
                    for element in progress_elements:
                        text = element.text
                        if '完成' in text or '优选' in text:
                            print("测试已完成")
                            return True
                
                # 检查结果列表
                result_elements = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'ip-list') or contains(@class, 'result')]")
                if result_elements:
                    print("检测到结果列表，测试可能已完成")
                    return True
                
                time.sleep(5)
                
            except Exception as e:
                print(f"检查测试进度时出错: {e}")
                time.sleep(5)
        
        print("测试等待超时")
        return False
    
    def append_save_ips(self):
        """追加保存优选IP"""
        try:
            print("正在追加保存优选IP...")
            
            button_selectors = [
                "//button[contains(text(), '追加保存优选IP')]",
                "//input[@value='追加保存优选IP']",
                "//button[contains(text(), '追加保存')]"
            ]
            
            button = None
            for selector in button_selectors:
                try:
                    button = self.wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                    break
                except TimeoutException:
                    continue
            
            if button:
                button.click()
                print("追加保存操作已执行")
                time.sleep(3)
                return True
            else:
                print("未找到追加保存按钮")
                return False
                
        except Exception as e:
            print(f"追加保存时出错: {e}")
            return False
    
    def get_test_results(self):
        """获取测试结果"""
        try:
            print("正在获取测试结果...")
            
            ip_elements = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'ip') or contains(text(), '.')]")
            
            results = []
            for element in ip_elements:
                text = element.text.strip()
                if text and '.' in text and len(text.split('.')) == 4:
                    results.append(text)
            
            print(f"获取到 {len(results)} 个IP结果")
            return results
            
        except Exception as e:
            print(f"获取测试结果时出错: {e}")
            return []
    
    def run_automation(self):
        """运行完整的自动化流程"""
        try:
            print("开始CloudFlare IP优选自动化流程（CF官方列表+443端口）...")
            
            # 1. 打开网站
            if not self.open_website():
                return False
            
            # 2. 清除所有选择
            if not self.clear_all_selections():
                print("清除选择失败")
                return False
            
            # 3. 选择CF官方列表
            if not self.select_cf_official():
                print("选择CF官方列表失败")
                return False
            
            # 4. 选择443端口
            if not self.select_port_443():
                print("选择443端口失败")
                return False
            
            # 5. 开始测试
            if not self.start_test():
                print("开始测试失败")
                return False
            
            # 6. 等待测试完成
            if not self.wait_for_test_completion():
                print("测试等待超时")
                return False
            
            # 7. 追加保存
            if not self.append_save_ips():
                print("追加保存失败")
                return False
            
            # 8. 获取结果
            results = self.get_test_results()
            
            # 9. 保存到文件
            if results:
                self.save_results_to_file(results)
            
            print("自动化流程完成")
            return True
            
        except Exception as e:
            print(f"自动化流程执行出错: {e}")
            return False
        finally:
            if self.driver:
                self.driver.quit()
                print("浏览器已关闭")
    
    def save_results_to_file(self, results):
        """保存结果到文件"""
        try:
            if not results:
                print("没有结果可保存")
                return False
            
            # 追加保存到ip.txt文件
            with open('ip.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n# CF官方列表优选IP - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"# 获取到 {len(results)} 个优选IP\n")
                f.write(f"# {'='*50}\n")
                for ip in results:
                    f.write(f"{ip}\n")
            
            print(f"结果已保存到 ip.txt 文件，共 {len(results)} 个IP")
            return True
            
        except Exception as e:
            print(f"保存结果到文件时出错: {e}")
            return False

def main():
    """主函数"""
    print("CloudFlare IP优选自动化工具（CF官方列表+443端口）")
    print("=" * 50)
    
    # 检查是否在代理环境中
    print("⚠️  请确保您当前未使用代理或VPN，以确保测试结果准确")
    
    automation = CFIPAutomation()
    success = automation.run_automation()
    
    if success:
        print("✅ 自动化执行成功")
    else:
        print("❌ 自动化执行失败")

if __name__ == "__main__":
    main()
