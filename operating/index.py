import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from operating.dbop import DB

# UI - Logic 分离

ui, _ = loadUiType('../staticUI/mainwindow.ui')


class MainApp(QMainWindow, ui):
    ispooled = False
    usern = ""
    usertyp = ""
    usertel = ""

    # d定义构造方法
    def __init__(self, usern, usertel, usertyp):
        QMainWindow.__init__(self)
        self.usertyp = usertyp
        self.usertel = usertel
        self.usern = usern
        self.setupUi(self)
        self.handle_ui_change()
        self.handle_buttons()
        # self.show_route()

        print(self.usertyp)
        print(self.usern)
        print(self.usertel)

    # UI动态加载
    def handle_ui_change(self):
        #  tabbar 的隐藏
        self.tabWidget.tabBar().setVisible(True)
        self.textBrowser_2.append(self.usertyp)
        self.tableWidget_3.horizontalHeader().resizeSection(1, 170)  # 调整列的大小为100像素
        self.tableWidget_3.horizontalHeader().resizeSection(2, 170)
        self.tableWidget_4.horizontalHeader().resizeSection(1, 170)  # 调整列的大小为100像素
        self.tableWidget_4.horizontalHeader().resizeSection(2, 170)
        self.tableWidget_6.horizontalHeader().resizeSection(2, 170)  # 调整列的大小为100像素
        self.tableWidget_6.horizontalHeader().resizeSection(3, 170)
        self.tableWidget_6.horizontalHeader().resizeSection(0, 40)  # 调整列的大小为100像素
        self.tableWidget_6.horizontalHeader().resizeSection(4, 40)  # 调整列的大小为100像素
        self.tableWidget_11.horizontalHeader().resizeSection(2, 170)  # 调整列的大小为100像素
        self.tableWidget_11.horizontalHeader().resizeSection(3, 170)
        self.tableWidget_11.horizontalHeader().resizeSection(0, 40)  # 调整列的大小为100像素
        self.tableWidget_11.horizontalHeader().resizeSection(4, 40)  # 调整列的大小为100像素

        self.tableWidget.horizontalHeader().resizeSection(0, 60)  # 调整列的大小为100像素
        self.tableWidget.horizontalHeader().resizeSection(2, 90)
        self.tableWidget.horizontalHeader().resizeSection(3, 100)  # 调整列的大小为100像素
        self.tableWidget.horizontalHeader().resizeSection(4, 110)  # 调整列的大小为100像素
        self.tableWidget.horizontalHeader().resizeSection(5, 90)  # 调整列的大小为100像素
        self.tableWidget_2.horizontalHeader().resizeSection(0, 60)  # 调整列的大小为100像素
        self.tableWidget_2.horizontalHeader().resizeSection(2, 90)
        self.tableWidget_2.horizontalHeader().resizeSection(3, 100)  # 调整列的大小为100像素
        self.tableWidget_2.horizontalHeader().resizeSection(4, 110)  # 调整列的大小为100像素
        self.tableWidget_2.horizontalHeader().resizeSection(5, 90)  # 调整列的大小为100像素
        if self.usertyp == "乘客":
            self.tabWidget_2.setTabEnabled(1, False)
            self.tabWidget_2.setTabEnabled(2, False)
            self.tabWidget_3.setTabEnabled(2, False)
            self.tabWidget_3.setTabEnabled(3, False)
            self.tabWidget_4.setTabEnabled(1, False)
            self.tabWidget_4.setTabEnabled(2, False)
            self.tabWidget_4.setTabEnabled(3, False)
        else:
            if self.usertyp == "司机":
                self.tabWidget_3.setTabEnabled(2, False)
                self.tabWidget_3.setTabEnabled(3, False)

    # 处理Button的消息与槽函数的绑定
    def handle_buttons(self):
        # 选项卡联动
        self.orderbutton.clicked.connect(self.open_oder_tab)
        self.routebutton.clicked.connect(self.open_route_tab)
        self.driverbutton.clicked.connect(self.open_driver_tab)
        self.detailbutton_2.clicked.connect(self.open_info_tab)
        # 路线管理
        self.initiatebutton_2.clicked.connect(self.add_route)
        self.serchbutton_3.clicked.connect(self.show_route)
        self.serchbutton_4.clicked.connect(self.show_route3)
        self.serchbutton_5.clicked.connect(self.show_route2)
        self.pushButton_4.clicked.connect(self.delete_route)
        self.pushButton_3.clicked.connect(self.alter_route)
        self.serchbutton_8.clicked.connect(self.serch_route)
        self.initiatebutton_3.clicked.connect(self.add_driver)
        self.serchbutton_6.clicked.connect(self.show_driver)
        self.serchbutton_13.clicked.connect(self.serch_driver)
        self.serchbutton_18.clicked.connect(self.show_driver3)
        self.pushButton_10.clicked.connect(self.alter_driver)
        self.serchbutton_7.clicked.connect(self.show_driver4)
        self.pushButton_5.clicked.connect(self.delete_driver)
        self.exitbutton.clicked.connect(self.quit)
        self.serchbutton.clicked.connect(self.show_order)
        self.pushButton.clicked.connect(self.carpool)
        self.initiatebutton.clicked.connect(self.new_order)
        self.serchbutton_9.clicked.connect(self.update_order)
        self.serchbutton_2.clicked.connect(self.show_order2)
        self.pushButton_2.clicked.connect(self.delete_order)

    def open_oder_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def open_route_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def open_driver_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def open_info_tab(self):
        self.tabWidget.setCurrentIndex(3)

    # Logic 层

    # 数据库处理:路线部分
    def add_route(self):
        lineedit_start = self.lineEdit_8.text()
        lineedit_end = self.lineEdit_9.text()
        lineedit_length = self.lineEdit_10.text()
        d = DB()
        if lineedit_start and lineedit_end and lineedit_length:
            sql = "insert into route(start,end,length) values(%s,%s,%s)"
            d.fix_db(sql, (lineedit_start, lineedit_end, lineedit_length))
            # 显示信息
            self.statusBar().showMessage("路线添加成功")
            # self.show_route()
        else:
            QMessageBox.warning(self, "添加路线", "请完善您的信息!",
                                QMessageBox.Yes)

    def show_route(self):
        d = DB()
        sql = "select * from route"
        result = d.search_db(sql)
        # print(result)
        if result:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(result):
                # print(row, form)
                for column, item in enumerate(form):
                    # print(row, column, item)
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_3.rowCount()
                # print(row_position+"rowposition")
                self.tableWidget_3.insertRow(row_position)
        self.statusBar().showMessage("路线查询成功")

    def show_route2(self):
        d = DB()
        sql = "select * from route"
        result = d.search_db(sql)
        # print(result)
        if result:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(result):
                # print(row, form)
                for column, item in enumerate(form):
                    # print(row, column, item)
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_4.rowCount()
                # print(row_position+"rowposition")
                self.tableWidget_4.insertRow(row_position)
        self.statusBar().showMessage("路线查询成功")

    def show_route3(self):
        old_id = self.lineEdit_7.text()
        # print(old_id)
        d = DB()
        sql = "select * from route where id = %s"
        result = d.search_db(sql, (str(old_id),))
        # print(result[0][1])
        if result:
            self.lineEdit_17.setText(str(result[0][1]))
            self.lineEdit_18.setText(str(result[0][2]))
            self.lineEdit_19.setText(str(result[0][3]))
        else:
            QMessageBox.warning(self, "修改路线", "路线不存在!",
                                QMessageBox.Yes)

    def alter_route(self):
        i = self.lineEdit_7.text()
        lineedit_start = self.lineEdit_17.text()
        lineedit_end = self.lineEdit_18.text()
        lineedit_length = self.lineEdit_19.text()
        d = DB()
        sql = "update route set start = %s,end = %s,length = %s where id = %s "
        d.fix_db(sql, (lineedit_start, lineedit_end, lineedit_length, i))
        self.statusBar().showMessage("路线修改成功")

    def delete_route(self):
        id_for_de = self.lineEdit_11.text()
        d = DB()
        sql = "select * from route where id = %s"
        result = d.search_db(sql, (str(id_for_de),))
        # print(result)
        if result:
            warning = QMessageBox.warning(self, "删除路线", "您确定要删除吗?",
                                          QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                sql = "delete from route where id = %s"
                d.fix_db(sql, (str(id_for_de),))
                self.statusBar().showMessage("删除路线成功")
                self.show_route2()
        else:
            QMessageBox.warning(self, "删除路线", "路线不存在!",
                                QMessageBox.Yes)

    def serch_route(self):
        info = self.lineEdit_20.text()
        # print(info)
        d = DB()
        sql = 'select * from route where(start like "%%"%s"%%" or end like "%%"%s"%%" or length like "%%"%s"%%" )'
        result = d.search_db(sql, (str(info), str(info), str(info)))
        # print(sql, (info, info, info))
        # print(result)
        if result:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(result):
                # print(row, form)
                for column, item in enumerate(form):
                    # print(row, column, item)
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_3.rowCount()
                # print(row_position+"rowposition")
                self.tableWidget_3.insertRow(row_position)
        self.statusBar().showMessage("特定路线查询成功")

    # 司机管理部分
    def add_driver(self):
        name = self.lineEdit_14.text()
        tel = self.lineEdit_13.text()
        ctype = self.lineEdit_12.text()
        limt = self.lineEdit_15.text()
        if name and tel and ctype and limt:
            d = DB()
            sql = "insert into driver(name,tel,cartype,limitedload) values (%s,%s,%s,%s)"
            d.fix_db(sql, (name, tel, ctype, limt))
            self.statusBar().showMessage("司机添加成功")
        else:
            QMessageBox.warning(self, "添加司机信息", "请完善您的信息!",
                                QMessageBox.Yes)

    def show_driver(self):
        d = DB()
        sql = "select * from driver"
        result = d.search_db(sql)
        # print(result)
        if result:
            self.tableWidget_6.setRowCount(0)
            self.tableWidget_6.insertRow(0)
            for row, form in enumerate(result):
                # print(row, form)
                for column, item in enumerate(form):
                    # print(row, column, item)
                    self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_6.rowCount()
                # print(row_position+"rowposition")
                self.tableWidget_6.insertRow(row_position)
        self.statusBar().showMessage("司机信息查询成功")

    def serch_driver(self):
        info = self.lineEdit_30.text()
        # print(info)
        d = DB()
        sql = 'select * from driver where(name like "%%"%s"%%" or ' \
              'tel like "%%"%s"%%" or cartype like "%%"%s"%%" or limitedload like "%%"%s"%%")'
        result = d.search_db(sql, (str(info), str(info), str(info), str(info)))
        # print(sql, (info, info, info))
        # print(result)
        if result:
            self.tableWidget_6.setRowCount(0)
            self.tableWidget_6.insertRow(0)
            for row, form in enumerate(result):
                # print(row, form)
                for column, item in enumerate(form):
                    # print(row, column, item)
                    self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_6.rowCount()
                # print(row_position+"rowposition")
                self.tableWidget_6.insertRow(row_position)
        self.statusBar().showMessage("特定司机信息询成功")

    def show_driver3(self):
        old_id = self.lineEdit_43.text()
        # print(old_id)
        d = DB()
        sql = "select * from driver where id = %s"
        result = d.search_db(sql, (str(old_id),))
        # print(result[0][1])
        if result:
            self.lineEdit_40.setText(str(result[0][1]))
            self.lineEdit_42.setText(str(result[0][2]))
            self.lineEdit_41.setText(str(result[0][3]))
            self.lineEdit_44.setText(str(result[0][4]))

        else:
            QMessageBox.warning(self, "修改司机信息", "司机信息不存在!",
                                QMessageBox.Yes)

    def show_driver4(self):
        d = DB()
        sql = "select * from driver"
        result = d.search_db(sql)
        # print(result)
        if result:
            self.tableWidget_11.setRowCount(0)
            self.tableWidget_11.insertRow(0)
            for row, form in enumerate(result):
                # print(row, form)
                for column, item in enumerate(form):
                    print(row, column, item)
                    self.tableWidget_11.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_11.rowCount()
                # print(row_position+"rowposition")
                self.tableWidget_11.insertRow(row_position)
        self.statusBar().showMessage("司机信息查询成功")

    def alter_driver(self):
        i = self.lineEdit_43.text()
        lineedit_start = self.lineEdit_40.text()
        lineedit_end = self.lineEdit_42.text()
        lineedit_length = self.lineEdit_41.text()
        lineedit_l = self.lineEdit_44.text()

        d = DB()
        sql = "update driver set name = %s,tel = %s, cartype = %s," \
              "limitedload = %s where id = %s "
        d.fix_db(sql, (lineedit_start, lineedit_end, lineedit_length, lineedit_l, i))
        self.statusBar().showMessage("司机信息修改成功")

    def delete_driver(self):
        id_for_de = self.lineEdit_16.text()
        d = DB()
        sql = "select * from driver where id = %s"
        result = d.search_db(sql, (str(id_for_de),))
        # print(result)
        if result:
            warning = QMessageBox.warning(self, "删除司机信息", "您确定要删除吗?",
                                          QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                sql = "delete from driver where id = %s"
                d.fix_db(sql, (str(id_for_de),))
                self.statusBar().showMessage("删除司机信息成功")
                self.show_route2()
        else:
            QMessageBox.warning(self, "删除司机信息", "路线不存在!",
                                QMessageBox.Yes)

    def delete_driver(self):
        id_for_de = self.lineEdit_16.text()
        d = DB()
        sql = "select * from driver where id = %s"
        result = d.search_db(sql, (str(id_for_de),))
        # print(result)
        if result:
            warning = QMessageBox.warning(self, "删除司机信息", "您确定要删除吗?",
                                          QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                sql = "delete from driver where id = %s"
                d.fix_db(sql, (str(id_for_de),))
                self.statusBar().showMessage("删除司机信息成功")
                self.show_driver4()
        else:
            QMessageBox.warning(self, "删除司机信息", "司机信息不存在!",
                                QMessageBox.Yes)

    def quit(self):
        self.close()

    # 订单管理部分
    def show_order(self):
        d = DB()
        sql = "select * from orderlist"
        result = d.search_db(sql)
        # print(result)
        if result:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            for row, form in enumerate(result):
                # print(row, form)
                for column, item in enumerate(form):
                    # print(row, column, item)
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget.rowCount()
                # print(row_position+"rowposition")
                self.tableWidget.insertRow(row_position)
        self.statusBar().showMessage("路线查询成功")

    def show_order2(self):
        d = DB()
        sql = "select * from orderlist"
        result = d.search_db(sql)
        # print(result)
        if result:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(result):
                # print(row, form)
                for column, item in enumerate(form):
                    # print(row, column, item)
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_2.rowCount()
                # print(row_position+"rowposition")
                self.tableWidget_2.insertRow(row_position)
        self.statusBar().showMessage("路线查询成功")

    def update_order(self):
        d = DB()
        sql = "select id from driver"
        result = d.search_db(sql)
        # print(result)
        for row, form in enumerate(result):
            # print(row, form)
            for column, item in enumerate(form):
                # print(row, column, item)
                self.comboBox.addItem(str(item))
                column += 1
            row += 1

        sql = "select id from route"
        result = d.search_db(sql)
        # print(result)
        for row, form in enumerate(result):
            # print(row, form)
            for column, item in enumerate(form):
                print(row, column, item)
                self.comboBox_2.addItem(str(item))
                column += 1
            row += 1
        self.statusBar().showMessage("x信息更新成功!")

    def new_order(self):
        driverid = self.comboBox.currentText()
        routeid = self.comboBox_2.currentText()
        limited = self.lineEdit_3.text()
        price = self.lineEdit_4.text()
        if driverid and routeid and limited and price:
            d = DB()
            sql = "insert into orderlist(driverid,limited,price,current,routeid) values (%s,%s,%s,0,%s)"
            d.fix_db(sql, (driverid, limited, price, routeid))

            self.statusBar().showMessage(" 订单发起成功")
        else:
            QMessageBox.warning(self, "发起拼单", "请您完善信息!",
                                QMessageBox.Yes)

    def delete_order(self):
        deleteid = self.lineEdit_6.text()
        d = DB()
        sql = "select * from orderlist where id = %s"
        result = d.search_db(sql, (str(deleteid),))
        # print(result)
        if result:
            warning = QMessageBox.warning(self, "删除拼单信息", "您确定要删除吗?",
                                          QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                sql = "delete from orderlist where id = %s"
                d.fix_db(sql, (str(deleteid),))
                self.statusBar().showMessage("删除订单信息成功")
                self.show_order2()
        else:
            QMessageBox.warning(self, "删除订单信息", "订单不存在!",
                                QMessageBox.Yes)

    def carpool(self):
        idd = self.lineEdit_5.text()
        if self.ispooled == False:
            d = DB()
            sql = "select name from driver where id in (select driverid from orderlist where id = %s)"
            drivername = d.search_db(sql, (idd,))
            sql = "select tel from driver where id in (select driverid from orderlist where id = %s)"
            drivertel = d.search_db(sql, (idd,))
            sql = "update orderlist set current = current+1 where id = %s"
            d.fix_db(sql, (idd,))
            sql = "select * from orderlist where id = %s"
            result = d.search_db(sql, (idd,))

            QMessageBox.warning(self, "确定拼车",
                                "拼车成功!\n请您信守承诺,尽快与司机取得联系,在约定地点及时上车.\n请记住您的拼车信息:\n拼车单号:" + idd + ";\n司机姓名:"
                                + drivername[0][0] + ";\n司机电话:" + drivertel[0][0] + ";\n\n乘客信息:\n乘客姓名:"
                                + self.usern + ";\n乘客电话:" + self.usertel + ";\n",
                                QMessageBox.Yes)
            self.ispooled = True
            sql = "insert into orderdetails(orderid,userid) values (%s,%s)"
            d.fix_db(sql, (idd, self.usern))
            self.statusBar().showMessage("订单详情记录成功")
            self.show_order()

            if int(result[0][2]) <= int(result[0][4]):
                QMessageBox.warning(self, "拼车", idd + "号订单已完成,即将销毁订单!",
                                    QMessageBox.Yes)
                sql = "delete from orderlist where id = %s"
                d.fix_db(sql, (idd,))

            self.show_order()
        else:
            QMessageBox.warning(self, "确定拼车", "您已经拼过了,请勿重复拼车!",
                                QMessageBox.Yes)


# d = DB()
# sql = "select * from driver "
# result = d.search_db(sql);
# print(result);


def main():
    app = QApplication([])
    window = MainApp('', '', '')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
