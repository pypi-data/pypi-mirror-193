from ...base import BaseRequest
 

class H5GetStartUrlRequest(BaseRequest):
    """
    
    :type dealer_id: string
    :param dealer_id: 平台企业 ID
    
    :type broker_id: string
    :param broker_id: 综合服务主体 ID
    
    :type dealer_user_id: string
    :param dealer_user_id: 平台企业端的用户 ID
    
    :type client_type: int
    :param client_type: 客户端类型
    
    :type notify_url: string
    :param notify_url: 异步通知 URL
    
    :type color: string
    :param color: H5 页面主题颜色
    
    :type return_url: string
    :param return_url: 跳转 URL
    
    :type custom_title: int
    :param custom_title: H5 页面 Title
    """
    def __init__(self, dealer_id=None, broker_id=None, dealer_user_id=None, client_type=None, notify_url=None, color=None, return_url=None, custom_title=None):
        super().__init__() 
        self.dealer_id = dealer_id 
        self.broker_id = broker_id 
        self.dealer_user_id = dealer_user_id 
        self.client_type = client_type 
        self.notify_url = notify_url 
        self.color = color 
        self.return_url = return_url 
        self.custom_title = custom_title

    def get_dealer_id(self):
        """ Get 平台企业 ID

        :return: string, dealer_id
        """
        return self.dealer_id

    def set_dealer_id(self, dealer_id):
        """ Set 平台企业 ID

        :type dealer_id: string
        :param dealer_id: 平台企业 ID
        """
        self.dealer_id = dealer_id

    def get_broker_id(self):
        """ Get 综合服务主体 ID

        :return: string, broker_id
        """
        return self.broker_id

    def set_broker_id(self, broker_id):
        """ Set 综合服务主体 ID

        :type broker_id: string
        :param broker_id: 综合服务主体 ID
        """
        self.broker_id = broker_id

    def get_dealer_user_id(self):
        """ Get 平台企业端的用户 ID

        :return: string, dealer_user_id
        """
        return self.dealer_user_id

    def set_dealer_user_id(self, dealer_user_id):
        """ Set 平台企业端的用户 ID

        :type dealer_user_id: string
        :param dealer_user_id: 平台企业端的用户 ID
        """
        self.dealer_user_id = dealer_user_id

    def get_client_type(self):
        """ Get 客户端类型

        :return: int, client_type
        """
        return self.client_type

    def set_client_type(self, client_type):
        """ Set 客户端类型

        :type client_type: int
        :param client_type: 客户端类型
        """
        self.client_type = client_type

    def get_notify_url(self):
        """ Get 异步通知 URL

        :return: string, notify_url
        """
        return self.notify_url

    def set_notify_url(self, notify_url):
        """ Set 异步通知 URL

        :type notify_url: string
        :param notify_url: 异步通知 URL
        """
        self.notify_url = notify_url

    def get_color(self):
        """ Get H5 页面主题颜色

        :return: string, color
        """
        return self.color

    def set_color(self, color):
        """ Set H5 页面主题颜色

        :type color: string
        :param color: H5 页面主题颜色
        """
        self.color = color

    def get_return_url(self):
        """ Get 跳转 URL

        :return: string, return_url
        """
        return self.return_url

    def set_return_url(self, return_url):
        """ Set 跳转 URL

        :type return_url: string
        :param return_url: 跳转 URL
        """
        self.return_url = return_url

    def get_custom_title(self):
        """ Get H5 页面 Title

        :return: int, custom_title
        """
        return self.custom_title

    def set_custom_title(self, custom_title):
        """ Set H5 页面 Title

        :type custom_title: int
        :param custom_title: H5 页面 Title
        """
        self.custom_title = custom_title 

class H5GetStartUrlResponse(BaseRequest):
    """
    
    :type h5_url: string
    :param h5_url: 跳转 URL
    """
    def __init__(self, h5_url=None):
        super().__init__() 
        self.h5_url = h5_url

    def get_h5_url(self):
        """ Get 跳转 URL

        :return: string, h5_url
        """
        return self.h5_url

    def set_h5_url(self, h5_url):
        """ Set 跳转 URL

        :type h5_url: string
        :param h5_url: 跳转 URL
        """
        self.h5_url = h5_url 

class H5EcoCityAicStatusRequest(BaseRequest):
    """
    
    :type dealer_id: string
    :param dealer_id: 平台企业 ID
    
    :type broker_id: string
    :param broker_id: 综合服务主体 ID
    
    :type dealer_user_id: string
    :param dealer_user_id: 平台企业端的用户 ID
    
    :type id_card: string
    :param id_card: 身份证号码
    
    :type real_name: string
    :param real_name: 姓名
    
    :type open_id: string
    :param open_id: 用户唯一标识
    """
    def __init__(self, dealer_id=None, broker_id=None, dealer_user_id=None, id_card=None, real_name=None, open_id=None):
        super().__init__() 
        self.dealer_id = dealer_id 
        self.broker_id = broker_id 
        self.dealer_user_id = dealer_user_id 
        self.id_card = id_card 
        self.real_name = real_name 
        self.open_id = open_id

    def get_dealer_id(self):
        """ Get 平台企业 ID

        :return: string, dealer_id
        """
        return self.dealer_id

    def set_dealer_id(self, dealer_id):
        """ Set 平台企业 ID

        :type dealer_id: string
        :param dealer_id: 平台企业 ID
        """
        self.dealer_id = dealer_id

    def get_broker_id(self):
        """ Get 综合服务主体 ID

        :return: string, broker_id
        """
        return self.broker_id

    def set_broker_id(self, broker_id):
        """ Set 综合服务主体 ID

        :type broker_id: string
        :param broker_id: 综合服务主体 ID
        """
        self.broker_id = broker_id

    def get_dealer_user_id(self):
        """ Get 平台企业端的用户 ID

        :return: string, dealer_user_id
        """
        return self.dealer_user_id

    def set_dealer_user_id(self, dealer_user_id):
        """ Set 平台企业端的用户 ID

        :type dealer_user_id: string
        :param dealer_user_id: 平台企业端的用户 ID
        """
        self.dealer_user_id = dealer_user_id

    def get_id_card(self):
        """ Get 身份证号码

        :return: string, id_card
        """
        return self.id_card

    def set_id_card(self, id_card):
        """ Set 身份证号码

        :type id_card: string
        :param id_card: 身份证号码
        """
        self.id_card = id_card

    def get_real_name(self):
        """ Get 姓名

        :return: string, real_name
        """
        return self.real_name

    def set_real_name(self, real_name):
        """ Set 姓名

        :type real_name: string
        :param real_name: 姓名
        """
        self.real_name = real_name

    def get_open_id(self):
        """ Get 用户唯一标识

        :return: string, open_id
        """
        return self.open_id

    def set_open_id(self, open_id):
        """ Set 用户唯一标识

        :type open_id: string
        :param open_id: 用户唯一标识
        """
        self.open_id = open_id 

class H5EcoCityAicStatusResponse(BaseRequest):
    """
    
    :type status: int
    :param status: 用户签约状态
    
    :type status_message: string
    :param status_message: 注册状态描述
    
    :type status_detail: int
    :param status_detail: 注册详情状态码
    
    :type status_detail_message: string
    :param status_detail_message: 注册详情状态码描述
    
    :type applyed_at: string
    :param applyed_at: 注册发起时间
    
    :type registed_at: string
    :param registed_at: 注册完成时间
    
    :type uscc: string
    :param uscc: 统一社会信用代码
    
    :type id_card: string
    :param id_card: 身份证号码
    
    :type real_name: string
    :param real_name: 姓名
    """
    def __init__(self, status=None, status_message=None, status_detail=None, status_detail_message=None, applyed_at=None, registed_at=None, uscc=None, id_card=None, real_name=None):
        super().__init__() 
        self.status = status 
        self.status_message = status_message 
        self.status_detail = status_detail 
        self.status_detail_message = status_detail_message 
        self.applyed_at = applyed_at 
        self.registed_at = registed_at 
        self.uscc = uscc 
        self.id_card = id_card 
        self.real_name = real_name

    def get_status(self):
        """ Get 用户签约状态

        :return: int, status
        """
        return self.status

    def set_status(self, status):
        """ Set 用户签约状态

        :type status: int
        :param status: 用户签约状态
        """
        self.status = status

    def get_status_message(self):
        """ Get 注册状态描述

        :return: string, status_message
        """
        return self.status_message

    def set_status_message(self, status_message):
        """ Set 注册状态描述

        :type status_message: string
        :param status_message: 注册状态描述
        """
        self.status_message = status_message

    def get_status_detail(self):
        """ Get 注册详情状态码

        :return: int, status_detail
        """
        return self.status_detail

    def set_status_detail(self, status_detail):
        """ Set 注册详情状态码

        :type status_detail: int
        :param status_detail: 注册详情状态码
        """
        self.status_detail = status_detail

    def get_status_detail_message(self):
        """ Get 注册详情状态码描述

        :return: string, status_detail_message
        """
        return self.status_detail_message

    def set_status_detail_message(self, status_detail_message):
        """ Set 注册详情状态码描述

        :type status_detail_message: string
        :param status_detail_message: 注册详情状态码描述
        """
        self.status_detail_message = status_detail_message

    def get_applyed_at(self):
        """ Get 注册发起时间

        :return: string, applyed_at
        """
        return self.applyed_at

    def set_applyed_at(self, applyed_at):
        """ Set 注册发起时间

        :type applyed_at: string
        :param applyed_at: 注册发起时间
        """
        self.applyed_at = applyed_at

    def get_registed_at(self):
        """ Get 注册完成时间

        :return: string, registed_at
        """
        return self.registed_at

    def set_registed_at(self, registed_at):
        """ Set 注册完成时间

        :type registed_at: string
        :param registed_at: 注册完成时间
        """
        self.registed_at = registed_at

    def get_uscc(self):
        """ Get 统一社会信用代码

        :return: string, uscc
        """
        return self.uscc

    def set_uscc(self, uscc):
        """ Set 统一社会信用代码

        :type uscc: string
        :param uscc: 统一社会信用代码
        """
        self.uscc = uscc

    def get_id_card(self):
        """ Get 身份证号码

        :return: string, id_card
        """
        return self.id_card

    def set_id_card(self, id_card):
        """ Set 身份证号码

        :type id_card: string
        :param id_card: 身份证号码
        """
        self.id_card = id_card

    def get_real_name(self):
        """ Get 姓名

        :return: string, real_name
        """
        return self.real_name

    def set_real_name(self, real_name):
        """ Set 姓名

        :type real_name: string
        :param real_name: 姓名
        """
        self.real_name = real_name 

class NotifyH5EcoCityAicRequest(BaseRequest):
    """
    
    :type open_id: string
    :param open_id: 用户唯一标识
    
    :type dealer_user_id: string
    :param dealer_user_id: 平台企业端的用户 ID
    
    :type submit_at: string
    :param submit_at: 注册/注销提交时间
    
    :type registed_at: string
    :param registed_at: 注册/注销完成时间
    
    :type status: int
    :param status: 用户签约状态
    
    :type status_message: string
    :param status_message: 注册状态描述
    
    :type status_detail: int
    :param status_detail: 注册详情状态码
    
    :type status_detail_message: string
    :param status_detail_message: 注册详情状态码描述
    
    :type dealer_id: string
    :param dealer_id: 平台企业 ID
    
    :type broker_id: string
    :param broker_id: 综合服务主体 ID
    
    :type uscc: string
    :param uscc: 统一社会信用代码
    
    :type id_card: string
    :param id_card: 身份证号码
    
    :type real_name: string
    :param real_name: 姓名
    
    :type type: int
    :param type: 回调类型
    """
    def __init__(self, open_id=None, dealer_user_id=None, submit_at=None, registed_at=None, status=None, status_message=None, status_detail=None, status_detail_message=None, dealer_id=None, broker_id=None, uscc=None, id_card=None, real_name=None, type=None):
        super().__init__() 
        self.open_id = open_id 
        self.dealer_user_id = dealer_user_id 
        self.submit_at = submit_at 
        self.registed_at = registed_at 
        self.status = status 
        self.status_message = status_message 
        self.status_detail = status_detail 
        self.status_detail_message = status_detail_message 
        self.dealer_id = dealer_id 
        self.broker_id = broker_id 
        self.uscc = uscc 
        self.id_card = id_card 
        self.real_name = real_name 
        self.type = type

    def get_open_id(self):
        """ Get 用户唯一标识

        :return: string, open_id
        """
        return self.open_id

    def set_open_id(self, open_id):
        """ Set 用户唯一标识

        :type open_id: string
        :param open_id: 用户唯一标识
        """
        self.open_id = open_id

    def get_dealer_user_id(self):
        """ Get 平台企业端的用户 ID

        :return: string, dealer_user_id
        """
        return self.dealer_user_id

    def set_dealer_user_id(self, dealer_user_id):
        """ Set 平台企业端的用户 ID

        :type dealer_user_id: string
        :param dealer_user_id: 平台企业端的用户 ID
        """
        self.dealer_user_id = dealer_user_id

    def get_submit_at(self):
        """ Get 注册/注销提交时间

        :return: string, submit_at
        """
        return self.submit_at

    def set_submit_at(self, submit_at):
        """ Set 注册/注销提交时间

        :type submit_at: string
        :param submit_at: 注册/注销提交时间
        """
        self.submit_at = submit_at

    def get_registed_at(self):
        """ Get 注册/注销完成时间

        :return: string, registed_at
        """
        return self.registed_at

    def set_registed_at(self, registed_at):
        """ Set 注册/注销完成时间

        :type registed_at: string
        :param registed_at: 注册/注销完成时间
        """
        self.registed_at = registed_at

    def get_status(self):
        """ Get 用户签约状态

        :return: int, status
        """
        return self.status

    def set_status(self, status):
        """ Set 用户签约状态

        :type status: int
        :param status: 用户签约状态
        """
        self.status = status

    def get_status_message(self):
        """ Get 注册状态描述

        :return: string, status_message
        """
        return self.status_message

    def set_status_message(self, status_message):
        """ Set 注册状态描述

        :type status_message: string
        :param status_message: 注册状态描述
        """
        self.status_message = status_message

    def get_status_detail(self):
        """ Get 注册详情状态码

        :return: int, status_detail
        """
        return self.status_detail

    def set_status_detail(self, status_detail):
        """ Set 注册详情状态码

        :type status_detail: int
        :param status_detail: 注册详情状态码
        """
        self.status_detail = status_detail

    def get_status_detail_message(self):
        """ Get 注册详情状态码描述

        :return: string, status_detail_message
        """
        return self.status_detail_message

    def set_status_detail_message(self, status_detail_message):
        """ Set 注册详情状态码描述

        :type status_detail_message: string
        :param status_detail_message: 注册详情状态码描述
        """
        self.status_detail_message = status_detail_message

    def get_dealer_id(self):
        """ Get 平台企业 ID

        :return: string, dealer_id
        """
        return self.dealer_id

    def set_dealer_id(self, dealer_id):
        """ Set 平台企业 ID

        :type dealer_id: string
        :param dealer_id: 平台企业 ID
        """
        self.dealer_id = dealer_id

    def get_broker_id(self):
        """ Get 综合服务主体 ID

        :return: string, broker_id
        """
        return self.broker_id

    def set_broker_id(self, broker_id):
        """ Set 综合服务主体 ID

        :type broker_id: string
        :param broker_id: 综合服务主体 ID
        """
        self.broker_id = broker_id

    def get_uscc(self):
        """ Get 统一社会信用代码

        :return: string, uscc
        """
        return self.uscc

    def set_uscc(self, uscc):
        """ Set 统一社会信用代码

        :type uscc: string
        :param uscc: 统一社会信用代码
        """
        self.uscc = uscc

    def get_id_card(self):
        """ Get 身份证号码

        :return: string, id_card
        """
        return self.id_card

    def set_id_card(self, id_card):
        """ Set 身份证号码

        :type id_card: string
        :param id_card: 身份证号码
        """
        self.id_card = id_card

    def get_real_name(self):
        """ Get 姓名

        :return: string, real_name
        """
        return self.real_name

    def set_real_name(self, real_name):
        """ Set 姓名

        :type real_name: string
        :param real_name: 姓名
        """
        self.real_name = real_name

    def get_type(self):
        """ Get 回调类型

        :return: int, type
        """
        return self.type

    def set_type(self, type):
        """ Set 回调类型

        :type type: int
        :param type: 回调类型
        """
        self.type = type