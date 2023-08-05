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


class CircleGeometryModel extends BaseGeometryModel {

    defaults() {
        return _.extend(BaseGeometryModel.prototype.defaults.call(this), {

            radius: 1,
            segments: 8,
            thetaStart: 0,
            thetaLength: 6.283185307179586,
            type: "CircleGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.CircleGeometry(
            this.convertFloatModelToThree(this.get('radius'), 'radius'),
            this.get('segments'),
            this.convertFloatModelToThree(this.get('thetaStart'), 'thetaStart'),
            this.convertFloatModelToThree(this.get('thetaLength'), 'thetaLength')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['radius'] = 'convertFloat';
        this.property_converters['segments'] = null;
        this.property_converters['thetaStart'] = 'convertFloat';
        this.property_converters['thetaLength'] = 'convertFloat';
        this.property_converters['type'] = null;


    }
}

CircleGeometryModel.model_name = 'CircleGeometryModel';
CircleGeometryModel.serializers = {
    ...BaseGeometryModel.serializers,
};

module.exports = {
    CircleGeometryModel: CircleGeometryModel,
};
