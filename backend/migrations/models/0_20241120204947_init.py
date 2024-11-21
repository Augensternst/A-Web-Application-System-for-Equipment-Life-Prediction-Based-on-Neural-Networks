from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `user` (
    `username` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT '用户名',
    `hashed_password` VARCHAR(128) NOT NULL  COMMENT '密码',
    `email` VARCHAR(50) NOT NULL  COMMENT '邮箱',
    `phone` VARCHAR(50) NOT NULL  COMMENT '电话',
    `role` INT NOT NULL  COMMENT '角色' DEFAULT 0,
    `avatar` LONGBLOB   COMMENT '头像'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `mmodel` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL UNIQUE COMMENT '模型名称',
    `style` VARCHAR(50) NOT NULL  COMMENT '模型风格' DEFAULT 'default',
    `uploaded_time` DATETIME(6) NOT NULL  COMMENT '上传时间' DEFAULT CURRENT_TIMESTAMP(6),
    `status` VARCHAR(10) NOT NULL  COMMENT '模型状态' DEFAULT '未知',
    `description` LONGTEXT NOT NULL  COMMENT '描述',
    `modelfile` LONGBLOB NOT NULL  COMMENT '模型文件',
    `md5` VARCHAR(32) NOT NULL UNIQUE COMMENT 'md5值',
    `user_id` VARCHAR(50) COMMENT '用户',
    CONSTRAINT `fk_mmodel_user_69801b5b` FOREIGN KEY (`user_id`) REFERENCES `user` (`username`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `component` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL  COMMENT '组件名称',
    `status` INT   COMMENT '组件状态',
    `life_forecast` INT NOT NULL  COMMENT '寿命预测' DEFAULT -1,
    `location` VARCHAR(50) NOT NULL  COMMENT '位置',
    `updated_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6),
    `pic` LONGBLOB   COMMENT '图片',
    `description` LONGTEXT   COMMENT '描述',
    `model_id` INT COMMENT '模型',
    `user_id` VARCHAR(50) NOT NULL COMMENT '用户',
    CONSTRAINT `fk_componen_mmodel_f4533986` FOREIGN KEY (`model_id`) REFERENCES `mmodel` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_componen_user_4f29eeaa` FOREIGN KEY (`user_id`) REFERENCES `user` (`username`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `ddata` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `file` LONGBLOB NOT NULL  COMMENT '数据文件',
    `name` VARCHAR(50)   COMMENT '数据名称',
    `time` DATETIME(6) NOT NULL  COMMENT '上传时间' DEFAULT CURRENT_TIMESTAMP(6),
    `result` LONGTEXT   COMMENT '结果',
    `component_id` INT NOT NULL COMMENT '组件',
    CONSTRAINT `fk_ddata_componen_27bd013d` FOREIGN KEY (`component_id`) REFERENCES `component` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
