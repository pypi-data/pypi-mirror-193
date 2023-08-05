//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseGeometryModel = require('../core/BaseGeometry.autogen.js').BaseGeometryModel;


class BoxGeometryModel extends BaseGeometryModel {

    defaults() {
        return _.extend(BaseGeometryModel.prototype.defaults.call(this), {

            width: 1,
            height: 1,
            depth: 1,
            widthSegments: 1,
            heightSegments: 1,
            depthSegments: 1,
            type: "BoxGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.BoxGeometry(
            this.convertFloatModelToThree(this.get('width'), 'width'),
            this.convertFloatModelToThree(this.get('height'), 'height'),
            this.convertFloatModelToThree(this.get('depth'), 'depth'),
            this.get('widthSegments'),
            this.get('heightSegments'),
            this.get('depthSegments')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['width'] = 'convertFloat';
        this.property_converters['height'] = 'convertFloat';
        this.property_converters['depth'] = 'convertFloat';
        this.property_converters['widthSegments'] = null;
        this.property_converters['heightSegments'] = null;
        this.property_converters['depthSegments'] = null;
        this.property_converters['type'] = null;


    }
}

BoxGeometryModel.model_name = 'BoxGeometryModel';
BoxGeometryModel.serializers = {
    ...BaseGeometryModel.serializers,
};

module.exports = {
    BoxGeometryModel: BoxGeometryModel,
};
