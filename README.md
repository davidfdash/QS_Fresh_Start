# QS_Fresh_Start
Get rid of dated Qlik Sense items

The intent is to assist customers with removing years of cruft.<br>

Variables contains the environmental variables so they do not need to be filled in on each script.

The certs can be created following instructions here:
https://community.qlik.com/t5/Official-Support-Articles/Call-the-Qlik-Sense-QRS-API-with-Python/ta-p/1715877

LicenseUsage is identifying users by their last license usage. This will create a csv file that will contain the user name, id, and the last time a license was used. Currently it checks for Professional/Analyzer licenses and tokens. The intent is to create a complementary script that will delete users based on the csv.

Apps <br>
appdates pulls all apps in the system with the name, id, and last time reloaded and puts that in a csv. delteApps is a complementary csv. The intent is to take the appReloadDates.csv generated by appDates, remove all apps you want to keep, and then save the csv as appsToDelete.csv. When run, deleteApps will delete the apps present in the appsToDelete.csv

data connections -

custom properties -
