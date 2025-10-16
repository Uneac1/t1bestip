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
        if os.getenv('GITHUB_ACTIONS'):
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.7390.107 Safari/537.36')
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, 20)
            print("Chrome浏览器驱动初始化成功")
        else:
            self.driver = None
            self.wait = None
            print("本地环境，跳过Chrome初始化")
    
    def open_website(self):
        """打开优选IP网站"""
        if not self.driver:
            print("本地环境，跳过网站访问")
            return True
        
        print("正在打开优选IP网站...")
        self.driver.get('https://t1.y130.icu/t1/bestip')
        time.sleep(5)
        print("网站加载完成")
        return True
    
    def select_cf_official(self):
        """检查CF官方列表是否已选中"""
        if not self.driver:
            print("本地环境，跳过CF官方列表检查")
            return True
        
        print("正在检查CF官方列表选择...")
        
        try:
            # 查找IP库输入框，检查当前值
            ip_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'IP库') or contains(@class, 'ip-library')]")
            current_value = ip_input.get_attribute('value')
            
            if 'CF官方列表' in current_value:
                print("CF官方列表已选中")
                return True
            else:
                print(f"当前IP库选择: {current_value}")
                # 如果未选中，尝试点击下拉框选择
                dropdown_arrow = self.driver.find_element(By.XPATH, "//div[contains(@class, 'dropdown') or contains(@class, 'select')]//button[contains(@class, 'arrow') or contains(@class, 'chevron')]")
                dropdown_arrow.click()
                time.sleep(1)
                
                # 选择CF官方列表
                cf_option = self.driver.find_element(By.XPATH, "//option[contains(text(), 'CF官方列表')]")
                cf_option.click()
                print("已选择CF官方列表")
                return True
                
        except Exception as e:
            print(f"CF官方列表检查失败: {e}")
            return False
    
    def select_port_443(self):
        """选择443端口"""
        if not self.driver:
            print("本地环境，跳过端口选择")
            return True
        
        print("正在选择443端口...")
        
        try:
            # 查找端口输入框
            port_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, '端口') or contains(@class, 'port')]")
            current_value = port_input.get_attribute('value')
            
            if '443' in current_value:
                print("443端口已选中")
                return True
            else:
                print(f"当前端口选择: {current_value}")
                # 点击端口下拉框
                port_dropdown = self.driver.find_element(By.XPATH, "//div[contains(@class, 'dropdown') or contains(@class, 'select')]//button[contains(@class, 'arrow') or contains(@class, 'chevron')]")
                port_dropdown.click()
                time.sleep(1)
                
                # 选择443端口
                port_443 = self.driver.find_element(By.XPATH, "//option[contains(text(), '443')]")
                port_443.click()
                print("已选择443端口")
                return True
                
        except Exception as e:
            print(f"443端口选择失败: {e}")
            return False
    
    def start_test(self):
        """开始延迟测试"""
        if not self.driver:
            print("本地环境，跳过延迟测试")
            return True
        
        print("正在开始延迟测试...")
        
        try:
            # 查找开始测试按钮
            start_button = self.driver.find_element(By.XPATH, "//button[contains(text(), '开始延迟测试')]")
            start_button.click()
            print("延迟测试已开始")
            return True
            
        except Exception as e:
            print(f"开始测试失败: {e}")
            return False
    
    def wait_for_test_completion(self):
        """等待测试完成，每10秒检查一次"""
        if not self.driver:
            print("本地环境，跳过测试等待")
            return True
        
        print("等待测试完成...")
        
        max_wait_time = 300  # 最大等待5分钟
        check_interval = 10  # 每10秒检查一次
        elapsed_time = 0
        
        while elapsed_time < max_wait_time:
            try:
                # 检查测试进度
                progress_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), '测试进度')]")
                for element in progress_elements:
                    text = element.text
                    if '完成' in text:
                        print("测试已完成")
                        return True
                
                # 检查IP列表是否已加载
                ip_list_elements = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'ip-list') or contains(@id, 'ip')]")
                if ip_list_elements:
                    ip_text = ip_list_elements[0].text
                    if ip_text and '请选择端口和IP库' not in ip_text and len(ip_text.strip()) > 0:
                        print("IP列表已加载")
                        return True
                
                print(f"测试进行中... 已等待 {elapsed_time} 秒")
                time.sleep(check_interval)
                elapsed_time += check_interval
                
            except Exception as e:
                print(f"检查测试状态时出错: {e}")
                time.sleep(check_interval)
                elapsed_time += check_interval
        
        print("测试等待超时")
        return False
    
    def get_test_results(self):
        """获取测试结果"""
        if not self.driver:
            print("本地环境，无法获取真实测试结果")
            return None
        
        print("正在获取测试结果...")
        
        try:
            # 获取统计信息
            stats_info = self.get_stats_info()
            
            # 获取测试进度
            progress_info = self.get_progress_info()
            
            # 获取IP列表
            ip_list = self.get_ip_list()
            
            if not ip_list:
                print("获取IP列表失败")
                return None
            
            results = {
                'stats': stats_info,
                'progress': progress_info,
                'ips': ip_list
            }
            
            print(f"获取到 {len(ip_list)} 个IP结果")
            return results
            
        except Exception as e:
            print(f"获取测试结果失败: {e}")
            return None
    
    def get_stats_info(self):
        """获取统计信息"""
        try:
            # 查找统计信息区域
            stats_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), '统计信息') or contains(text(), '获取到的IP总数') or contains(text(), '您的国家')]")
            if stats_elements:
                return stats_elements[0].text.strip()
            return "统计信息获取失败"
        except:
            return "统计信息获取失败"
    
    def get_progress_info(self):
        """获取测试进度"""
        try:
            # 查找测试进度区域
            progress_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), '测试进度') or contains(text(), '完成')]")
            if progress_elements:
                return progress_elements[0].text.strip()
            return "测试进度获取失败"
        except:
            return "测试进度获取失败"
    
    def get_ip_list(self):
        """获取IP列表"""
        try:
            # 查找IP列表区域
            ip_list_elements = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'ip-list') or contains(@id, 'ip') or contains(@class, 'result')]")
            
            if not ip_list_elements:
                print("未找到IP列表区域")
                return []
            
            ip_list_text = ip_list_elements[0].text
            print(f"IP列表原始文本: {ip_list_text[:200]}...")
            
            # 按行分割并提取IP
            lines = ip_list_text.split('\n')
            results = []
            
            for line in lines:
                line = line.strip()
                if line and '.' in line:
                    # 提取IP地址（去除延迟信息）
                    parts = line.split()
                    for part in parts:
                        if '.' in part and len(part.split('.')) == 4:
                            # 验证IP格式
                            ip_parts = part.split('.')
                            if len(ip_parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in ip_parts):
                                if part not in results:
                                    results.append(part)
                                    break
            
            return results
            
        except Exception as e:
            print(f"获取IP列表失败: {e}")
            return []
    
    def save_results_to_file(self, results):
        """保存结果到文件"""
        if not results:
            print("没有结果可保存")
            return False
        
        with open('ip.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n# CF官方列表优选IP - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# 统计信息: {results.get('stats', '获取失败')}\n")
            f.write(f"# 测试进度: {results.get('progress', '获取失败')}\n")
            f.write(f"# {'='*50}\n")
            
            for ip in results.get('ips', []):
                f.write(f"{ip}\n")
        
        print(f"结果已保存到 ip.txt 文件，共 {len(results.get('ips', []))} 个IP")
        return True
    
    def run_automation(self):
        """运行完整的自动化流程"""
        try:
            print("开始CloudFlare IP优选自动化流程...")
            
            # 1. 打开网站
            if not self.open_website():
                return False
            
            # 2. 检查CF官方列表
            if not self.select_cf_official():
                return False
            
            # 3. 选择443端口
            if not self.select_port_443():
                return False
            
            # 4. 开始测试
            if not self.start_test():
                return False
            
            # 5. 等待测试完成
            if not self.wait_for_test_completion():
                return False
            
            # 6. 获取结果
            results = self.get_test_results()
            if not results:
                return False
            
            # 7. 保存到文件
            if not self.save_results_to_file(results):
                return False
            
            print("自动化流程完成")
            return True
            
        except Exception as e:
            print(f"自动化流程执行出错: {e}")
            return False
        finally:
            if self.driver:
                self.driver.quit()
                print("浏览器已关闭")

def main():
    """主函数"""
    print("CloudFlare IP优选自动化工具")
    print("=" * 50)
    
    automation = CFIPAutomation()
    success = automation.run_automation()
    
    if success:
        print("自动化执行成功")
    else:
        print("自动化执行失败")

if __name__ == "__main__":
    main()