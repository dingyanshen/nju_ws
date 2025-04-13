;; Auto-generated. Do not edit!


(when (boundp 'camera::PhotoService)
  (if (not (find-package "CAMERA"))
    (make-package "CAMERA"))
  (shadow 'PhotoService (find-package "CAMERA")))
(unless (find-package "CAMERA::PHOTOSERVICE")
  (make-package "CAMERA::PHOTOSERVICE"))
(unless (find-package "CAMERA::PHOTOSERVICEREQUEST")
  (make-package "CAMERA::PHOTOSERVICEREQUEST"))
(unless (find-package "CAMERA::PHOTOSERVICERESPONSE")
  (make-package "CAMERA::PHOTOSERVICERESPONSE"))

(in-package "ROS")





(defclass camera::PhotoServiceRequest
  :super ros::object
  :slots (_shelf_id ))

(defmethod camera::PhotoServiceRequest
  (:init
   (&key
    ((:shelf_id __shelf_id) "")
    )
   (send-super :init)
   (setq _shelf_id (string __shelf_id))
   self)
  (:shelf_id
   (&optional __shelf_id)
   (if __shelf_id (setq _shelf_id __shelf_id)) _shelf_id)
  (:serialization-length
   ()
   (+
    ;; string _shelf_id
    4 (length _shelf_id)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _shelf_id
       (write-long (length _shelf_id) s) (princ _shelf_id s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _shelf_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _shelf_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass camera::PhotoServiceResponse
  :super ros::object
  :slots (_provinces _positions_x _positions_y ))

(defmethod camera::PhotoServiceResponse
  (:init
   (&key
    ((:provinces __provinces) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:positions_x __positions_x) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:positions_y __positions_y) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _provinces __provinces)
   (setq _positions_x __positions_x)
   (setq _positions_y __positions_y)
   self)
  (:provinces
   (&optional __provinces)
   (if __provinces (setq _provinces __provinces)) _provinces)
  (:positions_x
   (&optional __positions_x)
   (if __positions_x (setq _positions_x __positions_x)) _positions_x)
  (:positions_y
   (&optional __positions_y)
   (if __positions_y (setq _positions_y __positions_y)) _positions_y)
  (:serialization-length
   ()
   (+
    ;; string[] _provinces
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _provinces)) 4
    ;; float32[] _positions_x
    (* 4    (length _positions_x)) 4
    ;; float32[] _positions_y
    (* 4    (length _positions_y)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _provinces
     (write-long (length _provinces) s)
     (dolist (elem _provinces)
       (write-long (length elem) s) (princ elem s)
       )
     ;; float32[] _positions_x
     (write-long (length _positions_x) s)
     (dotimes (i (length _positions_x))
       (sys::poke (elt _positions_x i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _positions_y
     (write-long (length _positions_y) s)
     (dotimes (i (length _positions_y))
       (sys::poke (elt _positions_y i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _provinces
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _provinces (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _provinces i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; float32[] _positions_x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _positions_x (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _positions_x i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _positions_y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _positions_y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _positions_y i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(defclass camera::PhotoService
  :super ros::object
  :slots ())

(setf (get camera::PhotoService :md5sum-) "16caea922424b37c40c5b1fe9cbf0c1b")
(setf (get camera::PhotoService :datatype-) "camera/PhotoService")
(setf (get camera::PhotoService :request) camera::PhotoServiceRequest)
(setf (get camera::PhotoService :response) camera::PhotoServiceResponse)

(defmethod camera::PhotoServiceRequest
  (:response () (instance camera::PhotoServiceResponse :init)))

(setf (get camera::PhotoServiceRequest :md5sum-) "16caea922424b37c40c5b1fe9cbf0c1b")
(setf (get camera::PhotoServiceRequest :datatype-) "camera/PhotoServiceRequest")
(setf (get camera::PhotoServiceRequest :definition-)
      "

string shelf_id
---
string[] provinces
float32[] positions_x
float32[] positions_y
")

(setf (get camera::PhotoServiceResponse :md5sum-) "16caea922424b37c40c5b1fe9cbf0c1b")
(setf (get camera::PhotoServiceResponse :datatype-) "camera/PhotoServiceResponse")
(setf (get camera::PhotoServiceResponse :definition-)
      "

string shelf_id
---
string[] provinces
float32[] positions_x
float32[] positions_y
")



(provide :camera/PhotoService "16caea922424b37c40c5b1fe9cbf0c1b")


