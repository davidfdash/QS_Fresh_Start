# QS_Fresh_Start
Get rid of dated Qlik Sense items

The intent is to assist customers with removing years of cruft.

LicenseUsage is identifying users by their last license usage. This will create a csv file that will contain the user name, id, and the last time a license was used. Currently it checks for Professional/Analyzer licenses and tokens. The intent is to create a complementary script that will delete users based on the csv.

appdates pulls all apps in the system with the name, id, and last time reloaded and puts that in a csv. The intent is to create a complementary script that will delete apps based on the csv.

data connections -

custom properties -
