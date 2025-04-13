// Auto-generated. Do not edit!

// (in-package camera.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class PhotoshelfServiceRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PhotoshelfServiceRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PhotoshelfServiceRequest
    let len;
    let data = new PhotoshelfServiceRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'camera/PhotoshelfServiceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PhotoshelfServiceRequest(null);
    return resolved;
    }
};

class PhotoshelfServiceResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.province_names = null;
      this.positions_x = null;
      this.positions_y = null;
      this.codes = null;
    }
    else {
      if (initObj.hasOwnProperty('province_names')) {
        this.province_names = initObj.province_names
      }
      else {
        this.province_names = [];
      }
      if (initObj.hasOwnProperty('positions_x')) {
        this.positions_x = initObj.positions_x
      }
      else {
        this.positions_x = [];
      }
      if (initObj.hasOwnProperty('positions_y')) {
        this.positions_y = initObj.positions_y
      }
      else {
        this.positions_y = [];
      }
      if (initObj.hasOwnProperty('codes')) {
        this.codes = initObj.codes
      }
      else {
        this.codes = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PhotoshelfServiceResponse
    // Serialize message field [province_names]
    bufferOffset = _arraySerializer.string(obj.province_names, buffer, bufferOffset, null);
    // Serialize message field [positions_x]
    bufferOffset = _arraySerializer.int32(obj.positions_x, buffer, bufferOffset, null);
    // Serialize message field [positions_y]
    bufferOffset = _arraySerializer.int32(obj.positions_y, buffer, bufferOffset, null);
    // Serialize message field [codes]
    bufferOffset = _arraySerializer.int32(obj.codes, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PhotoshelfServiceResponse
    let len;
    let data = new PhotoshelfServiceResponse(null);
    // Deserialize message field [province_names]
    data.province_names = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [positions_x]
    data.positions_x = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [positions_y]
    data.positions_y = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [codes]
    data.codes = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.province_names.forEach((val) => {
      length += 4 + val.length;
    });
    length += 4 * object.positions_x.length;
    length += 4 * object.positions_y.length;
    length += 4 * object.codes.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'camera/PhotoshelfServiceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5fbec0c698813ceefcd320f6e0b0177c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] province_names
    int32[] positions_x
    int32[] positions_y
    int32[] codes
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PhotoshelfServiceResponse(null);
    if (msg.province_names !== undefined) {
      resolved.province_names = msg.province_names;
    }
    else {
      resolved.province_names = []
    }

    if (msg.positions_x !== undefined) {
      resolved.positions_x = msg.positions_x;
    }
    else {
      resolved.positions_x = []
    }

    if (msg.positions_y !== undefined) {
      resolved.positions_y = msg.positions_y;
    }
    else {
      resolved.positions_y = []
    }

    if (msg.codes !== undefined) {
      resolved.codes = msg.codes;
    }
    else {
      resolved.codes = []
    }

    return resolved;
    }
};

module.exports = {
  Request: PhotoshelfServiceRequest,
  Response: PhotoshelfServiceResponse,
  md5sum() { return '5fbec0c698813ceefcd320f6e0b0177c'; },
  datatype() { return 'camera/PhotoshelfService'; }
};
