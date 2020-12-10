PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('7344a1e6cfcc');
CREATE TABLE admin (
	user_id VARCHAR(64) NOT NULL, 
	email VARCHAR(128), 
	password_hash VARCHAR(128), 
	PRIMARY KEY (user_id)
);
INSERT INTO admin VALUES('test','test@test.com','pbkdf2:sha256:150000$WMO0Y2qk$48a19ed1bcd4363f96c8ebb9d6e54dd9ad75442e5fa2ae96534c1dc67f96a2b3');
INSERT INTO admin VALUES('test2','test2@test.com','pbkdf2:sha256:150000$iIq6Ew0d$186458e171b903b9597a6f2f9c12e504046a245bbdb058af04f25ac2ea8e7a4f');
INSERT INTO admin VALUES('190422294','190422294@stu.vtc.edu.hk','pbkdf2:sha256:150000$4Zl77HmN$87c3fa59c97e3e3f131a9f6b7ee88fd6c684d9fdfdbe2269c7e92cce94b6472e');
CREATE TABLE home_about_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	image VARCHAR(256), 
	content VARCHAR(1024), 
	link VARCHAR(256), 
	link_text VARCHAR(64), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO home_about_block VALUES(1,'What is ASP.NET?','https://dotnet.microsoft.com/static/images/illustrations/swimlane-aspnet-extends-dotnet.svg?v=ZcDShBF9nHCAmwWukmLbPca-qgxgVpdWLQBl7eOU1Ac',replace(replace('.NET is a developer platform made up of tools, programming languages, and libraries for building many different types of applications.\r\n</p><p>\r\nASP.NET extends the .NET developer platform with tools and libraries specifically for building web apps.','\r',char(13)),'\n',char(10)),'https://dotnet.microsoft.com/learn/aspnet/what-is-aspnet','Dig deeper: What is ASP.NET?','190422294','2020-04-29 12:54:27.127399');
INSERT INTO home_about_block VALUES(2,'Learn ASP.NET','https://dotnet.microsoft.com/static/images/illustrations/swimlane-subscribe-to-news-tips.svg?v=A94E1l9TIWsCIkmDeropAHlbiplQlriIi_BUbDW-rjE','Learn about all ASP.NET has to offer with our tutorials, video courses, and docs.','https://dotnet.microsoft.com/learn/aspnet','Learn to use ASP.NET','test','2020-04-29 12:16:42.831338');
INSERT INTO home_about_block VALUES(3,'Fast and scalable','https://dotnet.microsoft.com/static/images/redesign/shared/tech-empower-results.svg?v=EttLBPxhbKrp7sGA5uKOujUvnbqYSSRNuIqEol0jNok','ASP.NET performs faster than any popular web framework in the independent TechEmpower benchmarks.','','','test','2020-04-29 12:17:44.456690');
INSERT INTO home_about_block VALUES(4,'Build secure apps','https://dotnet.microsoft.com/static/images/illustrations/swimlane-security.svg?v=1Gm-V54l8uhuOvWY_EbAX8vwGvR89i7qv04Hdqu5DqA',replace(replace('ASP.NET supports industry standard authentication protocols. Built-in features help protect your apps against cross-site scripting (XSS) and cross-site request forgery (CSRF).\r\n</p><p>\r\nASP.NET provides a built-in user database with support for multi-factor authentication and external authentication with Google, Twitter, and more.','\r',char(13)),'\n',char(10)),'','','190422294','2020-04-29 12:54:55.075168');
INSERT INTO home_about_block VALUES(5,'Active community and open-source','https://dotnet.microsoft.com/static/images/illustrations/swimlane-community-documentation.svg?v=ZCPKmQRCzLBNOmu00jNggqSUQbxRbNzguW9OZuDl2Tw',replace(replace('Get quick answers to questions with an active community of developers on StackOverflow, ASP.NET forums, and more.\r\n</p><p>\r\nASP.NET is open source on GitHub, with over 60,000 developers and 3,700 companies already contributing.\r\n\r\n','\r',char(13)),'\n',char(10)),'https://dotnet.microsoft.com/platform/community','Join the ASP.NET community','190422294','2020-04-29 12:55:15.398032');
INSERT INTO home_about_block VALUES(6,'Free hosting on Azure','https://dotnet.microsoft.com/static/images/illustrations/spot-azure-accessible-everywhere.svg?v=-kiBh7KO-r83yu7cvskbHanLcQWnyB-5su_MKpfZm4o',replace(replace('Get 10 ASP.NET websites for free with Microsoft Azure.\r\n</p><p>\r\nYou can also deploy to any major cloud platform, your own Linux or Windows servers, or one of many hosting providers.','\r',char(13)),'\n',char(10)),'https://azure.microsoft.com/services/app-service/web/','Host for free with Azure','190422294','2020-04-29 12:55:32.815661');
CREATE TABLE home_client_block (
	id INTEGER NOT NULL, 
	client_logo VARCHAR(256), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO home_client_block VALUES(1,'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Stack_Overflow_logo.svg/1920px-Stack_Overflow_logo.svg.png','test','2020-04-29 12:20:36.936510');
INSERT INTO home_client_block VALUES(2,'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/UPS_Logo_Shield_2017.svg/800px-UPS_Logo_Shield_2017.svg.png','test','2020-04-29 12:20:54.072383');
INSERT INTO home_client_block VALUES(3,'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Alaska_Airlines_logo.svg/1920px-Alaska_Airlines_logo.svg.png','test','2020-04-29 12:21:19.540777');
INSERT INTO home_client_block VALUES(4,'https://upload.wikimedia.org/wikipedia/commons/2/23/Jetcom_logo15.png','test','2020-04-29 12:21:46.976532');
INSERT INTO home_client_block VALUES(5,'https://dotnet.microsoft.com/blob-assets/images/customers/raygun.svg?v=qfl8S-DOMZ4z70geS6_vPOum6ZOUZcseSq3gBGv3CUk','test','2020-04-29 12:22:51.041317');
CREATE TABLE home_functions_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	icon VARCHAR(256), 
	content VARCHAR(256), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO home_functions_block VALUES(1,'Web Apps','','Build pages based on HTML5, CSS, and JavaScript, using C# for server-side logic','190422294','2020-04-29 12:38:45.489858');
INSERT INTO home_functions_block VALUES(2,'APIs','','Develop REST APIs for a range of clients, including browsers and mobile devices','test','2020-04-29 12:14:52.423482');
INSERT INTO home_functions_block VALUES(3,'Real-time','','Enable bi-directional communication between server and client, in real-time','test','2020-04-29 12:15:04.433372');
INSERT INTO home_functions_block VALUES(4,'Microservices','','Create independently deployable microservices that run on Docker containers','test','2020-04-29 12:15:24.508496');
CREATE TABLE about_net_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	media VARCHAR(1024), 
	content VARCHAR(1024), 
	link VARCHAR(256), 
	link_text VARCHAR(64), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO about_net_block VALUES(1,'.NET',replace(replace('<div class="embed-responsive embed-responsive-16by9">\r\n    <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/eIHKZfgddLM?list=PLdo4fOcmZ0oWoazjhXQzBKMrFuArxpW80" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\r\n</div>','\r',char(13)),'\n',char(10)),replace(replace('<p>.NET is a free, cross-platform, open source developer platform for building many different types of applications.</p>\r\n<p>With .NET, you can use multiple languages, editors, and libraries to build for web, mobile, desktop, gaming, and IoT.</p>','\r',char(13)),'\n',char(10)),'','','190422294','2020-12-07 12:19:55.737388');
INSERT INTO about_net_block VALUES(2,'Languages','<div style="height: 200px; background-image: url(''https://dotnet.microsoft.com/static/images/redesign/shared/languages.svg?v=yvShriMWFIRrnXnWH5qXijlyXm2mceVpo7nF0qmS9j8''); background-size: contain; background-position: center; background-repeat: no-repeat;"></div>',replace(replace('<p>You can write .NET apps in C#, F#, or Visual Basic.</p>\r\n<ul class="pl-18">\r\n    <li>C# is a simple, modern, object-oriented, and type-safe programming language.</li>\r\n    <li>F# is a cross-platform, open-source, functional programming language for .NET. It also includes object-oriented and imperative programming.</li>\r\n    <li>Visual Basic is an approachable language with a simple syntax for building type-safe, object-oriented apps.</li>\r\n</ul>','\r',char(13)),'\n',char(10)),'https://dotnet.microsoft.com/languages','Learn about .NET Languages','190422294','2020-04-29 14:15:11.631557');
INSERT INTO about_net_block VALUES(3,'Cross Platform','<div style="height: 200px; background-image: url(''https://dotnet.microsoft.com/static/images/redesign/learn/what-is-dotnet/cross-platform.svg?v=anfPiIBTMTvKH8bexRWIiCVlrs1QmV5FHDb96PaoVCw''); background-size: contain; background-position: center; background-repeat: no-repeat;"></div>',replace(replace('<p>Whether you''re working in C#, F#, or Visual Basic, your code will run natively on any compatible OS. Different .NET implementations handle the heavy lifting for you:</p>\r\n<ul>\r\n    <li>.NET Core is a cross-platform .NET implementation for websites, servers, and console apps on Windows, Linux, and macOS.</li>\r\n    <li>.NET Framework supports websites, services, desktop apps, and more on Windows.</li>\r\n    <li>Xamarin/Mono is a .NET implementation for running apps on all the major mobile operating systems.</li>\r\n</ul>','\r',char(13)),'\n',char(10)),'','','test2','2020-04-29 14:44:31.415005');
INSERT INTO about_net_block VALUES(4,'One consistent API','<div style="height: 200px; background-image: url(''https://dotnet.microsoft.com/static/images/redesign/shared/platform.svg?v=1AekG8sFoRFIXTRNH81pNfUInvmmA-ouVdZ3XwmpqlE''); background-size: contain; background-position: center; background-repeat: no-repeat;"></div>',replace(replace('<p>.NET Standard is a base set of APIs that are common to all .NET implementations.</p>\r\n<p>Each implementation can also expose additional APIs that are specific to the operating systems it runs on. For example, .NET Framework is a Windows-only .NET implementation that includes APIs for accessing the Windows Registry.</p>','\r',char(13)),'\n',char(10)),'https://dotnet.microsoft.com/platform/dotnet-standard','Learn about .NET Standard','190422294','2020-04-29 14:20:37.804441');
INSERT INTO about_net_block VALUES(5,'Libraries','<div style="height: 200px; background-image: url(''https://dotnet.microsoft.com/static/images/redesign/learn/what-is-dotnet/packages.svg?v=6lmZ7JRNHAyIR1jkLeY6iC95AiW3nNqqBwiSLLUdbG8''); background-size: contain; background-position: center; background-repeat: no-repeat;"></div>','<p>To extend functionality, Microsoft and others maintain a healthy package ecosystem built on .NET Standard.</p><p>NuGet is a package manager built specifically for .NET that contains over 90,000 packages.</p>','','','190422294','2020-04-29 14:43:36.046661');
INSERT INTO about_net_block VALUES(6,'Active community and open-source',replace(replace('\r\n<div style="height: 200px; background-image: url(''https://dotnet.microsoft.com/static/images/illustrations/swimlane-contributors-around-world-no-text.svg?v=6rndqKzGUY9c0CNwIi-3uBciYuklIqID_YR_97RfZ_0''); background-size: contain; background-position: center; background-repeat: no-repeat;"></div>','\r',char(13)),'\n',char(10)),replace(replace('<p>.NET is open source and under the .NET Foundation. The .NET Foundation is an independent organization to foster open development and collaboration around the .NET ecosystem.</p>\r\n\r\n<p>Because .NET is open source, you can join the 60,000 developers and 3,700 companies already contributing to the .NET platform.</p>\r\n\r\n<p>Get quick answers to questions with an active community of developers on StackOverflow.</p>','\r',char(13)),'\n',char(10)),'https://dotnet.microsoft.com/platform/community','Join the .NET community','190422294','2020-04-29 14:26:09.232285');
INSERT INTO about_net_block VALUES(7,'Tools','<div style="height: 200px; background-image: url(''https://dotnet.microsoft.com/static/images/redesign/shared/tools.svg?v=LliEomktjf8LKEuN7tLJ2y4zJ75I-K81auaZCGBpaKs''); background-size: contain; background-position: center; background-repeat: no-repeat;"></div>',replace(replace('<p>The Visual Studio product family provides a great .NET development experience on Windows, Linux, and macOS.</p>\r\n\r\n<p>The Visual Studio Marketplace has thousands of editor extensions from Microsoft and others.</p>\r\n\r\n<p>If you prefer to use a different editor, there are .NET command line tools and plugins for many popular editors.</p>','\r',char(13)),'\n',char(10)),'https://dotnet.microsoft.com/platform/tools','Learn about tools for .NET','190422294','2020-04-29 14:27:38.235921');
INSERT INTO about_net_block VALUES(8,'Why choose .NET?','<div style="height: 200px; background-image: url(''https://dotnet.microsoft.com/static/images/redesign/customers/more-stories.svg?v=fChPtOnskvbYW-ZEwYG6bdEZLxmG2gMnNcQ9O6kp9vM''); background-size: contain; background-position: center; background-repeat: no-repeat;"></div>','<p>Find out why customers all over the world, in many different industries, rely on .NET.</p>','https://dotnet.microsoft.com/platform/why-choose-dotnet','Why choose .NET?','190422294','2020-04-29 14:29:11.136371');
CREATE TABLE architecture_item_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	content VARCHAR(1024), 
	link VARCHAR(256), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO architecture_item_block VALUES(1,'Microservices','Build resilient, scalable, and independently deployable microservices using .NET and Docker.','https://dotnet.microsoft.com/learn/aspnet/microservices-architecture','190422294','2020-12-07 13:09:16.046449');
INSERT INTO architecture_item_block VALUES(2,'DevOps','DevOps and application lifecycle best practices for your .NET applications.','https://dotnet.microsoft.com/learn/aspnet/devops','190422294','2020-12-07 14:00:29.374348');
INSERT INTO architecture_item_block VALUES(3,'Modernizing web & server','Options for modernizing your existing web and server applications for the cloud.','https://dotnet.microsoft.com/apps/cloud/migrate-to-azure','190422294','2020-12-07 14:06:46.374333');
INSERT INTO architecture_item_block VALUES(4,'Azure cloud apps','Build production-ready cloud applications for scalability, security, resiliency, and more using Azure.','https://dotnet.microsoft.com/learn/azure/architecture','test2','2020-12-07 14:07:33.765526');
INSERT INTO architecture_item_block VALUES(5,'ASP.NET apps','Quickly build, test, and deploy data-driven web applications using the ASP.NET web framework.','https://dotnet.microsoft.com/learn/aspnet/architecture','test2','2020-12-07 14:07:53.666161');
INSERT INTO architecture_item_block VALUES(6,'Mobile apps','Build apps for iOS, Android, and Windows using .NET. Leverage native APIs on every platform while maximizing code-sharing across all of them.','https://dotnet.microsoft.com/learn/xamarin/architecture','test2','2020-12-07 14:08:13.253276');
INSERT INTO architecture_item_block VALUES(7,'UWP desktop apps','Build modern desktop experiences that empower your customers to do more with the Universal Windows Platform (UWP).','https://dotnet.microsoft.com/learn/desktop/architecture','test2','2020-12-07 14:08:41.095669');
CREATE TABLE architecture_ebook_block (
	id INTEGER NOT NULL, 
	cover_url VARCHAR(256), 
	link VARCHAR(256), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO architecture_ebook_block VALUES(1,'https://dotnet.microsoft.com/blob-assets/images/e-books/cloud-native-azure.png','https://dotnet.microsoft.com/learn/azure/architecture#ebook-cloud-native-azure-swimlane','test','2020-12-08 13:19:51.577597');
INSERT INTO architecture_ebook_block VALUES(2,'https://dotnet.microsoft.com/blob-assets/images/e-books/blazor-for-web-forms-devs.png','https://dotnet.microsoft.com/learn/aspnet/architecture#ebook-blazor-for-web-forms-devs-swimlane','test','2020-12-08 13:20:14.920336');
INSERT INTO architecture_ebook_block VALUES(3,'https://dotnet.microsoft.com/blob-assets/images/e-books/grpc-for-wcf-devs.png','https://dotnet.microsoft.com/learn/aspnet/architecture#ebook-grpc-for-wcf-devs-swimlane','test','2020-12-08 13:21:09.777667');
INSERT INTO architecture_ebook_block VALUES(4,'https://dotnet.microsoft.com/blob-assets/images/e-books/modernizing-existing-desktop-apps.png','https://dotnet.microsoft.com/learn/desktop/architecture#ebook-modernizing-existing-desktop-apps-swimlane','test','2020-12-08 13:21:24.050021');
CREATE TABLE learn_tutor_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	content VARCHAR(1024), 
	link VARCHAR(256), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO learn_tutor_block VALUES(1,'Console','Build a simple text-based application that runs in the console/terminal','https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/intro','test','2020-12-08 10:36:37.970344');
INSERT INTO learn_tutor_block VALUES(2,'In-browser Tutorial','Try .NET in your browser, without installing anything on your computer','https://dotnet.microsoft.com/learn/dotnet/in-browser-tutorial/1','test','2020-12-08 10:48:38.050684');
INSERT INTO learn_tutor_block VALUES(3,'Web','Create a web app that runs on Windows, Linux, macOS, and Docker','https://dotnet.microsoft.com/learn/aspnet/hello-world-tutorial/intro','test','2020-12-08 10:48:55.414288');
INSERT INTO learn_tutor_block VALUES(4,'Mobile','Build an app that dials numbers on iOS, Android, and Windows devices','https://dotnet.microsoft.com/learn/xamarin/hello-world-tutorial/intro','test','2020-12-08 10:49:16.853129');
INSERT INTO learn_tutor_block VALUES(5,'Desktop','Develop an expense tracking desktop application for Windows','https://docs.microsoft.com/dotnet/framework/wpf/getting-started/walkthrough-my-first-wpf-desktop-application','test','2020-12-08 10:49:36.929717');
INSERT INTO learn_tutor_block VALUES(6,'Game Development','Create a 3D spinning cube with Unity','https://dotnet.microsoft.com/learn/games/unity-tutorial/intro','test','2020-12-08 10:49:55.194494');
INSERT INTO learn_tutor_block VALUES(7,'Machine Learning','Build a machine learning model to classify iris flowers','https://dotnet.microsoft.com/learn/ml-dotnet/get-started-tutorial/intro','test','2020-12-08 10:50:14.290549');
INSERT INTO learn_tutor_block VALUES(8,'Internet of Things','Blink an LED light on your Raspberry Pi, or other single-board computer','https://github.com/Microsoft/Windows-iotcore-samples/tree/develop/Samples/HelloBlinky/CS','test','2020-12-08 10:50:34.383252');
CREATE TABLE learn_material_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	link VARCHAR(256), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO learn_material_block VALUES(3,'Desktop','https://docs.microsoft.com/dotnet/#create-your-application','test','2020-12-08 11:32:35.047033');
INSERT INTO learn_material_block VALUES(4,'Game Development','https://dotnet.microsoft.com/learn/games/unity-tutorial/intro','test','2020-12-08 11:33:02.491226');
INSERT INTO learn_material_block VALUES(5,'Machine Learning and AI','https://dotnet.microsoft.com/learn/ml-dotnet','test','2020-12-08 11:33:25.689709');
INSERT INTO learn_material_block VALUES(6,'IoT','https://docs.microsoft.com/windows/iot-core/','test','2020-12-08 11:34:33.101906');
INSERT INTO learn_material_block VALUES(7,'Cloud','https://docs.microsoft.com/dotnet/azure','test','2020-12-08 11:34:43.684970');
INSERT INTO learn_material_block VALUES(8,'C#','https://dotnet.microsoft.com/learn/csharp','test','2020-12-08 11:35:04.826141');
INSERT INTO learn_material_block VALUES(9,'F#','https://dotnet.microsoft.com/learn/fsharp/','test','2020-12-08 11:35:16.816636');
INSERT INTO learn_material_block VALUES(10,'Visual Basic','https://docs.microsoft.com/dotnet/visual-basic/','test','2020-12-08 11:35:45.505843');
CREATE TABLE learn_res_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	image VARCHAR(256), 
	content VARCHAR(1024), 
	link VARCHAR(256), 
	link_text VARCHAR(64), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO learn_res_block VALUES(1,'.NET 101 video series','https://dotnet.microsoft.com/static/images/illustrations/swimlane-subscribe-to-news-tips.svg?v=ucyC2XSDQ8mMnjeHAoB-xUptKVAhrNCwu_y5a_KMqN4','Explore videos on web, mobile, desktop, C#, machine learning, containers/docker, data access, and more.','https://dotnet.microsoft.com/learn/videos','View free video about the .NET developer platform.','test','2020-12-08 13:13:46.871414');
INSERT INTO learn_res_block VALUES(2,'Architecture guides','https://dotnet.microsoft.com/static/images/illustrations/swimlane-architecture-guides.svg?v=jC6ekNggsZkoEOs7OdR0oOacviiYY_s0RFhxiEjaj2Q','Free e-books, videos, and practical advice to help you build better apps with .NET.','https://dotnet.microsoft.com/learn/dotnet/architecture-guides','Learn about the different architecture options for .NET','test','2020-12-08 13:15:04.743407');
INSERT INTO learn_res_block VALUES(3,'What is .NET?','https://dotnet.microsoft.com/static/images/redesign/shared/developers-at-desk.svg?v=RfhnV44hH0Q_202oQCA8kzA_rab1UBQXbuMmiTyIaOk','.NET is a free, cross-platform, open source developer platform for building many different types of apps.','https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet','Learn more about .NET''s multiple languages, editors, and libraries.','test','2020-12-08 13:15:33.057548');
CREATE TABLE comm_method_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	image VARCHAR(256), 
	content VARCHAR(1024), 
	link VARCHAR(256), 
	link_text VARCHAR(64), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO comm_method_block VALUES(1,'.NET Live TV','https://dotnet.microsoft.com/static/images/illustrations/swimlane-dotnet-tv.svg?v=9qLr39AINmhPqT2QNuN4K8xqJktIo3PyUK9C3Iy-4hY','Participate in weekly live shows hosted by the .NET team on Twitch and YouTube. These are casual conversations about what''s happening across .NET, full of community content, demos, and live Q&A.','https://dotnet.microsoft.com/live','Watch Now','test','2020-12-08 14:13:35.431533');
INSERT INTO comm_method_block VALUES(2,'Meetups','https://dotnet.microsoft.com/static/images/community/meetup.svg?v=vB2_LD59fnw-sJd-ziJXMdjQWMkc4Xj9nQzGpteSaRM','.NET meetups are a great and fun way of meeting other like-minded developers, and joining one couldn''t be easier. Learn about tricks & tips, discover the latest .NET has to offer, or just come to be inspired.','https://dotnetfoundation.org/community/meetups','Find Meetups','test','2020-12-08 13:59:58.269657');
CREATE TABLE comm_platform_block (
	id INTEGER NOT NULL, 
	title VARCHAR(64), 
	icon VARCHAR(256), 
	content VARCHAR(1024), 
	link VARCHAR(256), 
	link_text VARCHAR(64), 
	editor_user_id VARCHAR(64), 
	edited_time DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(editor_user_id) REFERENCES admin (user_id)
);
INSERT INTO comm_platform_block VALUES(1,'GitHub','https://dotnet.microsoft.com/static/images/community/github.svg?v=z_hmg9JcZ5e6Q3jmy3858EUfWgovNwNGkoEjv9X1ODg','The official home of .NET on GitHub. It''s a great starting point to find many .NET open-source projects from Microsoft and the community.','ASP.NET (web dev)','ASP.NET (web dev)','test','2020-12-08 14:31:16.175934');
INSERT INTO comm_platform_block VALUES(2,'Twitter','https://dotnet.microsoft.com/static/images/community/twitter.svg?v=xVUc0PmjSpz-49aMW3s0rNIkC-TvoI-4VkPtdH7v8SE','Follow us to keep in touch with the team and get updates on new features, releases, and more.','https://twitter.com/aspnet','ASP.NET (web dev)','test','2020-12-08 14:34:21.511716');
INSERT INTO comm_platform_block VALUES(3,'Facebook','https://dotnet.microsoft.com/static/images/community/facebook.svg?v=Tqa2hCFlH_1sMqlYOsG3ODIsVlSUi6UdQTjp59LL-Wo','If you''re more of a Facebook fan, you can also find us on Facebook.','ASP.NET (web dev)','ASP.NET (web dev)','test','2020-12-08 14:35:17.599102');
CREATE UNIQUE INDEX ix_admin_email ON admin (email);
CREATE UNIQUE INDEX ix_admin_user_id ON admin (user_id);
COMMIT;
