/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50505
Source Host           : 127.0.0.1:3306
Source Database       : inno_career

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2014-12-04 13:43:31
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `catalog`
-- ----------------------------
DROP TABLE IF EXISTS `catalog`;
CREATE TABLE `catalog` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录id',
  `name` varchar(50) NOT NULL COMMENT '查询代号, 字母. 用于一级',
  `title` varchar(255) NOT NULL COMMENT '显示名称',
  `parentId` int(11) NOT NULL DEFAULT '0' COMMENT '上层id',
  `orderNo` smallint(3) NOT NULL DEFAULT '100' COMMENT '显示顺序',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=utf8 COMMENT='常数表';

-- ----------------------------
-- Records of catalog
-- ----------------------------
INSERT INTO `catalog` VALUES ('28', 'company_property', '单位性质', '0', '10');
INSERT INTO `catalog` VALUES ('29', 'company_property', '行政单位', '28', '10');
INSERT INTO `catalog` VALUES ('30', 'company_property', '科研设计单位', '28', '20');
INSERT INTO `catalog` VALUES ('31', 'company_property', '高等学校', '28', '30');
INSERT INTO `catalog` VALUES ('32', 'company_property', '其它教学单位', '28', '31');
INSERT INTO `catalog` VALUES ('33', 'company_property', '医疗卫生单位', '28', '40');
INSERT INTO `catalog` VALUES ('34', 'company_property', '其它事业单位', '28', '41');
INSERT INTO `catalog` VALUES ('35', 'company_property', '国有企业', '28', '50');
INSERT INTO `catalog` VALUES ('36', 'company_property', '外资(欧美)', '28', '60');
INSERT INTO `catalog` VALUES ('37', 'company_property', '民营企业', '28', '70');
INSERT INTO `catalog` VALUES ('38', 'company_property', '其它企业', '28', '71');
INSERT INTO `catalog` VALUES ('39', 'company_property', '部队', '28', '80');
INSERT INTO `catalog` VALUES ('40', 'company_property', '其它', '28', '100');
INSERT INTO `catalog` VALUES ('41', 'industry', '行业类目', '0', '20');
INSERT INTO `catalog` VALUES ('42', 'industry', '计算机/互联网/通信/电子', '41', '100');
INSERT INTO `catalog` VALUES ('43', 'industry', '会计/金融/银行/保险', '41', '100');
INSERT INTO `catalog` VALUES ('44', 'industry', '贸易/消费/制造/营运', '41', '100');
INSERT INTO `catalog` VALUES ('45', 'industry', '制药/医疗', '41', '100');
INSERT INTO `catalog` VALUES ('46', 'industry', '广告/媒体', '41', '100');
INSERT INTO `catalog` VALUES ('47', 'industry', '房地产/建筑', '41', '100');
INSERT INTO `catalog` VALUES ('48', 'industry', '专业服务/教育/培训', '41', '100');
INSERT INTO `catalog` VALUES ('49', 'industry', '服务业', '41', '100');
INSERT INTO `catalog` VALUES ('50', 'industry', '物流/运输', '41', '100');
INSERT INTO `catalog` VALUES ('51', 'industry', '能源/原材料', '41', '100');
INSERT INTO `catalog` VALUES ('52', 'industry', '政府/非赢利机构', '41', '100');
INSERT INTO `catalog` VALUES ('53', 'industry', '其它', '41', '100');
INSERT INTO `catalog` VALUES ('54', 'industry', '计算机软件', '42', '100');
INSERT INTO `catalog` VALUES ('55', 'industry', '计算机硬件', '42', '100');
INSERT INTO `catalog` VALUES ('56', 'industry', '计算机服务(系统、数据服务、维修)', '42', '100');
INSERT INTO `catalog` VALUES ('57', 'industry', '通信/电信/网络设备', '42', '100');
INSERT INTO `catalog` VALUES ('58', 'industry', '通信/电信运营、增值服务', '42', '100');
INSERT INTO `catalog` VALUES ('59', 'industry', '互联网/电子商务', '42', '100');
INSERT INTO `catalog` VALUES ('60', 'industry', '网络游戏', '42', '100');
INSERT INTO `catalog` VALUES ('61', 'industry', '电子技术/半导体/集成电路', '42', '100');
INSERT INTO `catalog` VALUES ('62', 'industry', '仪器仪表/工业自动化', '42', '100');
INSERT INTO `catalog` VALUES ('63', 'industry', '会计/审计', '43', '100');
INSERT INTO `catalog` VALUES ('64', 'industry', '金融/投资/证券', '43', '100');
INSERT INTO `catalog` VALUES ('65', 'industry', '银行', '43', '100');
INSERT INTO `catalog` VALUES ('66', 'industry', '保险', '43', '100');
INSERT INTO `catalog` VALUES ('67', 'industry', '信托/担保/拍卖/典当', '43', '100');
INSERT INTO `catalog` VALUES ('68', 'industry', '贸易/进出口', '44', '100');
INSERT INTO `catalog` VALUES ('69', 'industry', '批发/零售', '44', '100');
INSERT INTO `catalog` VALUES ('70', 'industry', '快速消费品(食品、饮料、化妆品)', '44', '100');
INSERT INTO `catalog` VALUES ('71', 'industry', '服装/纺织/皮革', '44', '100');
INSERT INTO `catalog` VALUES ('72', 'industry', '家具/家电/玩具/礼品', '44', '100');
INSERT INTO `catalog` VALUES ('73', 'industry', '奢侈品/收藏品/工艺品/珠宝', '44', '100');
INSERT INTO `catalog` VALUES ('74', 'industry', '办公用品及设备', '44', '100');
INSERT INTO `catalog` VALUES ('75', 'industry', '机械/设备/重工', '44', '100');
INSERT INTO `catalog` VALUES ('76', 'industry', '汽车及零配件', '44', '100');
INSERT INTO `catalog` VALUES ('77', 'industry', '制药/生物工程', '45', '100');
INSERT INTO `catalog` VALUES ('78', 'industry', '医疗/护理/卫生', '45', '100');
INSERT INTO `catalog` VALUES ('79', 'industry', '医疗设备/器械', '45', '100');
INSERT INTO `catalog` VALUES ('80', 'industry', '广告', '46', '100');
INSERT INTO `catalog` VALUES ('81', 'industry', '公关/市场推广/会展', '46', '100');
INSERT INTO `catalog` VALUES ('82', 'industry', '影视/媒体/艺术/文化传播', '46', '100');
INSERT INTO `catalog` VALUES ('83', 'industry', '文字媒体/出版', '46', '100');
INSERT INTO `catalog` VALUES ('84', 'industry', '印刷/包装/造纸', '46', '100');
INSERT INTO `catalog` VALUES ('85', 'industry', '房地产开发', '47', '100');
INSERT INTO `catalog` VALUES ('86', 'industry', '建筑/建材/工程', '47', '100');
INSERT INTO `catalog` VALUES ('87', 'industry', '家居/室内设计/装潢', '47', '100');
INSERT INTO `catalog` VALUES ('88', 'industry', '物业管理/商业中心', '47', '100');
INSERT INTO `catalog` VALUES ('89', 'industry', '中介服务', '48', '100');
INSERT INTO `catalog` VALUES ('90', 'industry', '租赁服务', '48', '100');
INSERT INTO `catalog` VALUES ('91', 'industry', '专业服务(咨询、人力资源、财会)', '48', '100');
INSERT INTO `catalog` VALUES ('92', 'industry', '外包服务', '48', '100');
INSERT INTO `catalog` VALUES ('93', 'industry', '检测，认证', '48', '100');
INSERT INTO `catalog` VALUES ('94', 'industry', '法律', '48', '100');
INSERT INTO `catalog` VALUES ('95', 'industry', '教育/培训/院校', '48', '100');
INSERT INTO `catalog` VALUES ('96', 'industry', '学术/科研', '48', '100');
INSERT INTO `catalog` VALUES ('97', 'industry', '餐饮业', '49', '100');
INSERT INTO `catalog` VALUES ('98', 'industry', '酒店/旅游', '49', '100');
INSERT INTO `catalog` VALUES ('99', 'industry', '娱乐/休闲/体育', '49', '100');
INSERT INTO `catalog` VALUES ('100', 'industry', '美容/保健', '49', '100');
INSERT INTO `catalog` VALUES ('101', 'industry', '生活服务', '49', '100');
INSERT INTO `catalog` VALUES ('102', 'industry', '交通/运输/物流', '50', '100');
INSERT INTO `catalog` VALUES ('103', 'industry', '航天/航空', '50', '100');
INSERT INTO `catalog` VALUES ('104', 'industry', '石油/化工/矿产/地质', '51', '100');
INSERT INTO `catalog` VALUES ('105', 'industry', '采掘业/冶炼', '51', '100');
INSERT INTO `catalog` VALUES ('106', 'industry', '电气/电力/水利', '51', '100');
INSERT INTO `catalog` VALUES ('107', 'industry', '新能源', '51', '100');
INSERT INTO `catalog` VALUES ('108', 'industry', '原材料和加工', '51', '100');
INSERT INTO `catalog` VALUES ('109', 'industry', '政府/公共事业', '52', '100');
INSERT INTO `catalog` VALUES ('110', 'industry', '非盈利机构', '52', '100');
INSERT INTO `catalog` VALUES ('111', 'industry', '环保', '52', '100');
INSERT INTO `catalog` VALUES ('112', 'industry', '农/林/牧/渔', '52', '100');
INSERT INTO `catalog` VALUES ('113', 'industry', '多元化业务集团公司', '52', '100');
INSERT INTO `catalog` VALUES ('114', 'company_ecom', '企业经济类型', '0', '100');
INSERT INTO `catalog` VALUES ('115', 'company_ecom', '国有经济', '114', '100');
INSERT INTO `catalog` VALUES ('116', 'company_ecom', '集体经济', '114', '100');
INSERT INTO `catalog` VALUES ('117', 'company_ecom', '私营经济', '114', '100');
INSERT INTO `catalog` VALUES ('118', 'company_ecom', '个体经济', '114', '100');
INSERT INTO `catalog` VALUES ('119', 'company_ecom', '联营经济', '114', '100');
INSERT INTO `catalog` VALUES ('120', 'company_ecom', '股份制', '114', '100');
INSERT INTO `catalog` VALUES ('121', 'company_ecom', '外商投资', '114', '100');
INSERT INTO `catalog` VALUES ('122', 'company_ecom', '港澳台投资', '114', '100');
INSERT INTO `catalog` VALUES ('123', 'company_ecom', '其他', '114', '100');
INSERT INTO `catalog` VALUES ('124', 'company_scale', '企业规模', '0', '100');
INSERT INTO `catalog` VALUES ('125', 'company_scale', '少于50人', '124', '100');
INSERT INTO `catalog` VALUES ('126', 'company_scale', '50-150人', '124', '100');
INSERT INTO `catalog` VALUES ('127', 'company_scale', '150-500人', '124', '100');
INSERT INTO `catalog` VALUES ('128', 'company_scale', '500-1000人', '124', '100');
INSERT INTO `catalog` VALUES ('129', 'company_scale', '1000-5000人', '124', '100');
INSERT INTO `catalog` VALUES ('130', 'company_scale', '5000-10000人', '124', '100');
INSERT INTO `catalog` VALUES ('131', 'company_scale', '10000人以上', '124', '100');
INSERT INTO `catalog` VALUES ('132', 'degree', '学历', '0', '100');
INSERT INTO `catalog` VALUES ('133', 'degree', '博士', '132', '100');
INSERT INTO `catalog` VALUES ('134', 'degree', '硕士', '132', '100');
INSERT INTO `catalog` VALUES ('135', 'degree', '本科', '132', '100');
INSERT INTO `catalog` VALUES ('136', 'degree', '大专', '132', '100');
INSERT INTO `catalog` VALUES ('137', 'degree', '中专', '132', '100');
INSERT INTO `catalog` VALUES ('138', 'degree', '中技', '132', '100');
INSERT INTO `catalog` VALUES ('139', 'degree', '高中', '132', '100');
INSERT INTO `catalog` VALUES ('140', 'degree', '初中', '132', '100');
INSERT INTO `catalog` VALUES ('141', 'company_property', '外资(非欧美)', '28', '100');
INSERT INTO `catalog` VALUES ('142', 'company_property', '合资', '28', '100');
INSERT INTO `catalog` VALUES ('143', 'company_property', '国内上市公司', '28', '100');
INSERT INTO `catalog` VALUES ('144', 'company_property', '外企代表处', '28', '100');
