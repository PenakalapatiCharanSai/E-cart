-- SQLite Schema for SmartCart
-- Converted from MySQL Schema

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT,
  `email` TEXT UNIQUE,
  `password` TEXT
);

CREATE TABLE IF NOT EXISTS `admin` (
  `admin_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT,
  `email` TEXT UNIQUE,
  `password` TEXT,
  `profile_image` TEXT
);

CREATE TABLE IF NOT EXISTS `products` (
  `product_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `admin_id` INTEGER DEFAULT 1,
  `name` TEXT,
  `description` TEXT,
  `category` TEXT,
  `price` NUMERIC,
  `image` TEXT,
  `quantity` INTEGER DEFAULT 50,
  FOREIGN KEY (`admin_id`) REFERENCES `admin` (`admin_id`) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS `addresses` (
  `address_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER NOT NULL,
  `full_name` TEXT,
  `phone` TEXT,
  `street_address` TEXT,
  `city` TEXT,
  `state` TEXT,
  `pincode` TEXT,
  `is_default` INTEGER DEFAULT 0,
  FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER NOT NULL,
  `razorpay_order_id` TEXT,
  `razorpay_payment_id` TEXT,
  `amount` NUMERIC,
  `payment_status` TEXT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `address_id` INTEGER,
  `order_status` TEXT DEFAULT 'Placed',
  FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  FOREIGN KEY (`address_id`) REFERENCES `addresses` (`address_id`) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS `order_items` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `order_id` INTEGER NOT NULL,
  `product_id` INTEGER NOT NULL,
  `product_name` TEXT,
  `quantity` INTEGER,
  `price` NUMERIC,
  FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE,
  FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE
);
